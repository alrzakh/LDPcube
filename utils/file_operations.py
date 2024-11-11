import csv


def write_dict_to_csv(error_dictionary, avg_error_dictionary, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Protocol', 'Method', 'Repeat', 'Error'])

        for (p, m, i), postprocess_result in error_dictionary.items():
            writer.writerow([p, m, i, postprocess_result])

        for protocol, avg_error in avg_error_dictionary.items():
            writer.writerow([protocol, "N/A", "N/A", avg_error])
