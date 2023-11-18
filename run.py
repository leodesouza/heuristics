import os
from algorithms.scp import Scp

if __name__ == '__main__':
    module_directory = os.path.dirname(__file__)
    script_folder = 'data/scp'
    file_name = 'small_a.txt'
    path_file = os.path.join(module_directory, f'{script_folder}/{file_name}')

    scp = Scp()
    scp.open_file(path_file)
