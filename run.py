import os
import sys

from algorithms.scp import Scp
from algorithms.setcover.constructive import *


def main(argv):
    i = 1
    seed = 0
    scp_file = ''
    output_file = ''
    while i < len(argv):
        if argv[i] == '--seed':
            seed = int(argv[i + 1])
            i += 2
        elif argv[i] == '--output':
            output_file = argv[i + 1]
            i += 2
        else:
            print('\nERROR: parameter', argv[i], 'not recognized.')

    module_directory = os.path.dirname(__file__)
    script_folder = 'data/scp'
    file_name = 'small_a.txt'
    scp_file = os.path.join(module_directory, f'{script_folder}/{file_name}')
    scp = Scp()
    scp.open_file(scp_file)

    # scp.print_instance(1)
    scp_instance = scp.get_instance()
    print(f'SCP instance from file: {file_name}')
    print(scp_instance)
    print()
    print('#randomized constructive solution')
    solution = create_randomized_constructive(scp_instance)
    print(solution)
    print("\n")

    print('#greedy constructive solution')
    solution = create_greedy_constructive(scp_instance)
    print(solution)
    print("\n")

    print('#weighted greey constructive solution')
    solution = create_wighted_greedy_constructive(scp_instance)
    print(solution)


if __name__ == '__main__':
    main(sys.argv)
