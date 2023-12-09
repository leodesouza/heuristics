import os

# from algorithms import Scp
from algorithms.setcover.constructive import *


#def main(argv):
    # i = 1
    # seed = 0
    # scp_file = ''
    # output_file = ''
    # while i < len(argv):
    #     if argv[i] == '--seed':
    #         seed = int(argv[i + 1])
    #         i += 2
    #     elif argv[i] == '--output':
    #         output_file = argv[i + 1]
    #         i += 2
    #     else:
    #         print('\nERROR: parameter', argv[i], 'not recognized.')
    #
    # module_directory = os.path.dirname(__file__)
    # script_folder = 'data/scp'
    # file_name = 'small_a.txt'
    # scp_file = os.path.join(module_directory, f'{script_folder}/{file_name}')
    # scp = Scp()
    # scp.open_file(scp_file)
    # scp.print_instance(1)


# read parameters


if __name__ == '__main__':

    # main(sys.argv)

    elements = {1, 2, 3, 4, 5, 6, 7}
    sets = {
        'A': {1, 2, 3},
        'B': {2, 4, 5},
        'C': {1, 4, 6},
        'D': {3, 5, 7}
    }
    create_greedy_constructive(sets)
    create_randomized_constructive(sets)
    create_wighted_greedy_constructive(sets)

    # rd = Randomized()
    # result = rd.set_cover(elements, sets)

    # import itertools
    # mylist = [1, 2, 3]
    # permu = itertools.permutations(mylist)
    # print(list(permu))




