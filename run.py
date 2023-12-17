import os
import sys

from algorithms.config import Parameters
from algorithms.scp import Scp
from algorithms.setcover.constructive import *


def print_usage():
    print("\nUSAGE: run.py [param_name, param_value] [options]...\n")
    print("Parameters:")
    print("  --seed : seed to initialize random number generator")
    print("  --targetDir: Target directory with SCP files.")
    print("  --output: Filename for output results.")
    print("Options:")
    print("  --hc1: random solution construction")
    print("  --hc2: greedy solution construction")
    print("  --hc3: cost-based greedy solution construction")
    print("  --ch2: static cost-based greedy values.")
    print("  --re: applies redundancy elimination after construction.")
    print("  --bi: best improvement.")
    print("\n")


def read_parameters(argv):
    # /home/leonardosouza/projects/heuristics_files/scp/
    parameters = Parameters()
    i = 1
    while i < len(argv):
        if argv[i] == "--seed":
            parameters.seed = int(argv[i + 1])
            i += 2
        elif argv[i] == "--targetDir":
            parameters.target_dir = argv[i + 1]
            i += 2
        elif argv[i] == "--output":
            parameters.output_file = output_file = argv[i + 1]
            i += 2
        elif argv[i] == "--hc1":
            parameters.options.append('hc1')
            i += 1
        elif argv[i] == "--hc2":
            parameters.options.append('hc2')
            i += 1
        elif argv[i] == "--hc3":
            parameters.options.append('hc3')
            i += 1
        elif argv[i] == "--bi":
            parameters.options.append('bi')
            i += 1
        elif argv[i] == "--re":
            parameters.options.append('re')
            re = 1
            i += 1
        else:
            print(f"\nERROR: parameter {argv[i]} not recognized.\n")
            print_usage()
            sys.exit(1)
    return parameters


def main(argv):
    parameters = read_parameters(argv)
    if len(argv) <= 1:
        print_usage()
        return

    scp = Scp()
    scp.process_instances(parameters)


if __name__ == '__main__':
    main(sys.argv)
