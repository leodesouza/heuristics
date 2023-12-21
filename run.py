import os
import sys

from config import Parameters, MAX_EXPERIMENTS_ITERATIONS
from algorithms.scp_v2 import ScpV2


def print_usage():
    print("\nUSAGE: run.py [param_name, param_value] [options]...\n")
    print("Parameters:")
    print("  --seed : seed to initialize random number generator")
    print("  --source: source directory with SCP files.")
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
        elif argv[i] == "--source":
            parameters.source = argv[i + 1]
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
            i += 1
        elif argv[i] == "--localsearch":
            parameters.options.append('localsearch')
            i += 1
        elif argv[i] == "--grasp":
            parameters.options.append('grasp')
            i += 1
        elif argv[i] == "--itlocalsearch":
            parameters.options.append('itlocalsearch')
            i += 1
        elif argv[i] == "--sa":
            parameters.options.append('sa')
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
    scp = ScpV2()
    scp.process_instances(parameters, MAX_EXPERIMENTS_ITERATIONS)


if __name__ == '__main__':
    main(sys.argv)
