import os
import sys

from algorithms.scp import Scp


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
    scp.print_instance(1)
# read parameters


if __name__ == '__main__':
    main(sys.argv)
