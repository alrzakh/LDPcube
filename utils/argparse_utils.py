import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="LDP³: Post Processing methods for Local Differential Privacy.")

    available_protocols = ['grr', 'blh', 'olh', 'rappor', 'oue', 'subset']
    available_methods = ['base_pos', 'norm', 'norm_cut', 'norm_mul', 'norm_sub', 'power', 'power_ns']


    parser.add_argument(
        '-e', '--epsilon', 
        type=float, 
        help="Privacy parameter epsilon to use for the experiments."
    )
    parser.add_argument(
        '-p', '--protocol', 
        nargs='+', 
        help=f'LDP Protocol(s) to use. Use "all" to select all protocols: {available_protocols}.'
    )
    parser.add_argument(
        '-m', '--method', 
        nargs='+', 
        help=f'Post-Processing Method(s) to use. Use "all" to select all methods: {available_methods}.'
    )
    parser.add_argument(
        '-r', '--repeat', 
        type=int, 
        help="Number of repeats for the LDP aggregation. (e.g., 10)"
    )
    parser.add_argument(
        '-t', '--thread_number', 
        type=int, 
        help="Number of threads to run the experiments. (e.g., 5)"
    )
    parser.add_argument(
        '-d', '--dataset', 
        type=str, 
        help="Path to the dataset. Provide a valid file path (e.g., ./Datasets/DATA.csv)."
    )
    parser.add_argument(
        '-u', '--utility_metric', 
        type=str, 
        help="Utility metric to measure the error(s). Choose from: l1, l2, kl."
    )

    return parser
