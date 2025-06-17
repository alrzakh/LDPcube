import os
import time
import random
from copy import deepcopy
from collections import Counter

from concurrent import futures

import numpy as np

from protocols import grr, rappor, olh, oue, blh, subset
from protocols.variance import calculate_variances

from data_reader import read_dataset

from post_processing import norm, norm_mul, norm_cut, norm_sub, base_pos, power

from metrics import l1_error, l2_error, kl_divergence

from utils.argparse_utils import create_parser
from utils.file_operations import write_dict_to_csv
from utils.tabulation import print_table
from utils.calculate_win_counts import calculate_win_counts_and_percentages


def process_chunk(chunk, epsilon, perturb_func, aggregate_func, domain_size, seed):
    perturbed_data = []
    np.random.seed(seed)
    random.seed(seed)


    for dataPoint in chunk:
        perturbed_data.append(perturb_func(dataPoint, epsilon, domain_size))

    estimated_counts = aggregate_func(perturbed_data, epsilon, domain_size)

    return estimated_counts


def ldp(protocol, eps, thread_number, input_data, domain_size):

    mapping = {"grr": grr,
               "rappor": rappor,
               "olh": olh,
               "blh": blh,
               "subset": subset,
               "oue": oue}

    ldp_method = mapping[protocol]
    if isinstance(eps, (int, float)):
        epsilon_values = [eps]
    else:
        epsilon_values = eps

    data_chunks = np.array_split(input_data, thread_number)
    data_size = len(input_data)
    estimated_counts = []
    for eps in epsilon_values:

        results = []
        perturb_func = ldp_method.perturb
        aggregate_func = ldp_method.aggregate
        seeds = [random.randint(1, 100000000) for _ in range(thread_number)]
        with futures.ProcessPoolExecutor() as executor:
            jobs = [
                executor.submit(
                    process_chunk, chunk, eps, perturb_func, aggregate_func, domain_size, seed
                )
                for seed, chunk in zip(seeds, data_chunks)
            ]
            for job in futures.as_completed(jobs):
                results.append(job.result())
        estimated_counts = [sum(items) for items in zip(*results)]

    estimated_counts_normalized = [element / data_size for element in estimated_counts]

    return estimated_counts, estimated_counts_normalized


def postprocess(method, normalized_original, estimated_counts, estimated_counts_normalized, metric, original_data,
                epsilon, p):
    print(f'Post Processing started using {method} as method.')

    mapping = {
        "base_pos": base_pos,
        "norm": norm,
        "norm_cut": norm_cut,
        "norm_mul": norm_mul,
        "norm_sub": norm_sub,
        "power": power,
        "power_ns": power
    }

    post_process_func = mapping.get(method)
    if post_process_func is None:
        raise ValueError(f"Method '{method}' is not recognized.")

    domain = set(original_data)
    dom_size = len(domain)
    pop_size = len(original_data)

    if method in ['power', 'power_ns']:
        
        variance = calculate_variances(p, epsilon, dom_size, pop_size)

        post_data = post_process_func(estimated_counts, original_data, variance)
        if method == 'power_ns':
            post_data = norm_sub(post_data, normalized_original)
    else:
        post_data = post_process_func(estimated_counts_normalized, normalized_original)

   
    error = metric(post_data, normalized_original)

    return error


def find_lowest_error_percentage(data, p_key, n, method):

    filtered_data = {key: value for key, value in data.items() if key[0] == p_key}

    lowest_error_dict = {}
    method_count = {m: 0 for m in method}

    for key, value in filtered_data.items():
     
        i_key = key[2]
        m_key = key[1]

        if i_key not in lowest_error_dict or value < lowest_error_dict[i_key][1]:
            lowest_error_dict[i_key] = (m_key, value)

    for i_key, (method, _) in lowest_error_dict.items():
        method_count[method] += 1

    method_percentage = {method: (count / n) * 100 for method, count in method_count.items()}
    sorted_methods = sorted(method_percentage.items(), key=lambda x: x[1], reverse=True)

    return sorted_methods


def normalized_frequency_distribution(input_list):
    counts = Counter(input_list)

    unique_values = list(counts.keys())
    min_val = min(unique_values)
    max_val = max(unique_values)

    normalized_distributions = []
    for value in range(min_val, max_val + 1):
        normalized_frequency = counts.get(value, 0) / len(input_list)
        normalized_distributions.append(normalized_frequency)

    return normalized_distributions


if __name__ == '__main__':

    start = time.time()

    all_protocols = ["grr", "blh", "olh", "rappor", "oue", "subset"]
    all_methods = ["base_pos", "norm", "norm_cut", "norm_mul", "norm_sub", "power", "power_ns"]

    parser = create_parser()
    args = parser.parse_args()
    
    epsilon = args.epsilon
    repeats = args.repeat
    thread_number = args.thread_number
    dataset = args.dataset
    utility_metric = args.utility_metric

    protocols = all_protocols if "all" in args.protocol else args.protocol
    methods = all_methods if "all" in args.method else args.method

    if "all" in args.protocol and len(args.protocol) > 1:
        protocols = all_protocols
        print("Warning: 'all' overrides specific protocols. Using all protocols.")

    if "all" in args.method and len(args.method) > 1:
        methods = all_methods
        print("Warning: 'all' overrides specific methods. Using all methods.")

    full_directory = os.getcwd() + '/' + dataset

    file_name = os.path.basename(full_directory)
    dataset_name = os.path.splitext(file_name)[0]

    error_mapping = {
        "l1": l1_error,
        "l2": l2_error,
        "kl": kl_divergence
    }
    error_func = error_mapping.get(utility_metric.lower())
    if error_func is None:
        raise ValueError(f"Metric '{utility_metric}' is not recognized.")
    
    original_data, domain_size = read_dataset.read_data(full_directory)
    n = len(original_data)

    print('Settings:')
    print('Epsilon:', epsilon)
    print('Protocol:', protocols)
    print('Method:', methods)
    print('Repeat:', repeats)
    print('Thread Number:', thread_number)
    print('Dataset:', dataset_name)
    print('Dataset size:', n)
    print('Domain size:', domain_size)
    
    counts = Counter(original_data)
    counts_list = [counts.get(i, 0) for i in range(domain_size)]

    frequency = [counts.get(i, 0) / n for i in range(domain_size)]
    
    error_dictionary = {}
    error_without_pp = {p:[] for p in protocols}
    
    for i in range(repeats):
        estimate = []
        for p in protocols:
            print(f"For protocol {p.upper()} repeat number {i + 1} / {repeats} started.")

            estimated_counts, estimated_normal = ldp(p, epsilon, thread_number, deepcopy(original_data), domain_size)

            error_without_pp[p].append(error_func(estimated_normal, frequency))

            for m in methods:
                error_dictionary[(p, m, i)] = postprocess(m, frequency, estimated_counts, estimated_normal,
                                                            error_func, counts_list, epsilon, p)

    print(f'Time is: {time.time() - start}')
    
    avg_error_without_pp = {key: np.mean(values) for key, values in error_without_pp.items()}
    std_dev_without_pp = {key: round(np.std(values), 6) for key, values in error_without_pp.items()}
    
    
    answer_for_write = input("Do you want to write the results to a file? (Y/n)   ")
    if answer_for_write.lower() == "y" or answer_for_write.lower() == "yes":
        write_dict_to_csv(error_dictionary, error_without_pp, f'{dataset_name}_{utility_metric.upper()}.csv')
    
    win_counts, percentages, experiment_counts = calculate_win_counts_and_percentages(error_dictionary, repeats)

    answer = input("Do you want to draw a table for result? (Y/n)   ")
    if answer.lower() == "y" or answer.lower() == "yes":
        print_table(error_dictionary, percentages, avg_error_without_pp, std_dev_without_pp)


    for p, methods in win_counts.items():
        best_method, best_score = max(methods.items(), key=lambda item: item[1])
    
        print(f'For the protocol {p.upper()} out of {repeats} experiments, '
            f'{best_method.capitalize()} was the best PostProcessing Method with {(best_score/repeats) * 100} percentage.')
