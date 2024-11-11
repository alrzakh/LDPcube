from collections import defaultdict


def calculate_win_counts_and_percentages(error_dictionary, repeats):
    win_counts = defaultdict(lambda: defaultdict(int))
    percentages = {}
    experiment_counts = defaultdict(int)
    protocol_data = defaultdict(lambda: defaultdict(list))

    for (protocol, method, exp), error in error_dictionary.items():
        protocol_data[protocol][exp].append((method, error))
        experiment_counts[protocol] = max(experiment_counts[protocol], exp + 1)

    for protocol, experiments in protocol_data.items():
        for exp, methods in experiments.items():
            min_method = min(methods, key=lambda x: x[1])[0]
            win_counts[protocol][min_method] += 1

    all_methods = set([method for _, method, _ in error_dictionary.keys()])

    for protocol, methods in win_counts.items():
        total_experiments = experiment_counts[protocol]
        for method in all_methods:
            wins = methods.get(method, 0)
            win_percentage = (wins / total_experiments) * 100
            percentages[(protocol, method)] = win_percentage
    
    return win_counts, percentages, experiment_counts
