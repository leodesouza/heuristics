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
    subsets_and_costs = scp.get_subets_and_costs()
    print(f'SCP instance from file: {file_name}')
    print(subsets_and_costs)
    print()
    print('#randomized constructive solution')
    solution, total_cost = create_randomized_constructive(subsets_and_costs)
    print(f"Solution: {solution} and total cost: {total_cost}")
    print("\n")

    print('#greedy constructive solution')
    solution, total_cost = create_greedy_constructive(subsets_and_costs)
    print(solution, total_cost)
    print("\n")

    print('#weighted greey constructive solution')
    solution, total_cost = create_wighted_greedy_constructive(subsets_and_costs)
    print(solution, total_cost)


if __name__ == '__main__':
    main(sys.argv)
