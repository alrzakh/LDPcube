from tabulate import tabulate
import numpy as np


def print_table(result_dict, percentages, error_without_pp, std_dev_without_pp):
    
    error_data = {}


    for (protocol, method, repeat), error in result_dict.items():
        key = (protocol, method)
        if key not in error_data:
            error_data[key] = []
        error_data[key].append(error)

    table_data = []

    for (protocol, method), errors in error_data.items():
        avg_error = np.mean(errors)
        std_dev = round(np.std(errors), 6)
        
        
        win_rate = percentages[(protocol, method)]
        table_data.append([protocol.upper(), method.capitalize(), avg_error, std_dev, f"{win_rate:.2f}%"])

    for protocol, avg_error in error_without_pp.items():
        table_data.append([protocol.upper(), "Without PP", avg_error, std_dev_without_pp[protocol], "N/A"])

    headers = ["Protocol", "Method", "Avg_error", "Std_dev", "Win Rate"]
    
    table_data.sort(key=lambda x: (x[0], -float(x[4].rstrip('%')) if x[4] != "N/A" else float('-inf'), x[2] if isinstance(x[2], (int, float)) else float('inf')))
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    