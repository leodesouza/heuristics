import os
import time
from algorithms.setcover.constructive import randomized_constructive, greedy_constructive, weighted_greedy_constructive
from algorithms.config import Parameters
from algorithms.utils.pseudo_random_generator import lecuyer_rando


def write_to_file(instance_name, method_name, pseudo_random_generated, total_cost, cpu_time, output_file):
    with open(output_file, 'a', newline='') as file:
        file.writelines(f'{instance_name};{method_name};{pseudo_random_generated};{total_cost};{cpu_time}\n')


class Scp:

    def process_instances(self, parameters: Parameters):

        files = os.listdir(parameters.source)
        pseudo_random_generated = 0
        for file_name in files:
            if file_name == parameters.output_file:
                continue

            file_path = os.path.join(parameters.source, file_name)
            subsets = self.get_subsets(file_path)
            results = [([], 0)]  # list of all subsets with [([sub], cost)]
            constructive_method_name = ''
            # ** Start CPU Time **
            start_cpu_time = time.process_time()
            if 'hc1' in parameters.options:
                constructive_method_name = 'HC1'
                pseudo_random_generated = lecuyer_rando(parameters.seed)
                result = randomized_constructive.create_randomized_constructive(subsets, pseudo_random_generated)
            elif 'hc2' in parameters.options:
                constructive_method_name = 'HC2'
                result = greedy_constructive.create_greedy_constructive(subsets)
            elif 'hc3' in parameters.options:
                constructive_method_name = 'HC3'
                result = weighted_greedy_constructive.create_wighted_greedy_constructive(subsets)
            elif 're' in parameters.options:
                pass
            end_cpu_time = time.process_time()
            cpu_executation_time = (start_cpu_time - end_cpu_time)
            # ** End CPU Time **

            output_file = os.path.join(parameters.source, parameters.output_file)
            file_name, extension = os.path.splitext(file_name)
            write_to_file(file_name, constructive_method_name, pseudo_random_generated, result[1], cpu_executation_time, output_file)

    @staticmethod
    def get_subsets(scp_file):
        n = 0
        m = 0
        rows = []  # rows[i] that are covered by column i
        col = []  # col[i] columns that cover row i
        ncol = []  # ncol[i] number of columns that cover row i
        nrow = []  # nrow[i] number of rows that are covered by column i
        cost = []  # cost[i] cost of column i
        scp_file = scp_file
        with open(scp_file, 'r') as file:

            rows_columns_number = list(map(int, file.readline().split()))

            m = rows_columns_number[0]  # number of rows
            n = rows_columns_number[1]  # number of columns

            # cost of all columns
            cost = list(map(int, file.readline().split()))

            # Info of the columns that cover each row
            for i in range(m):

                ncol_i = int(file.readline().strip())
                ncol.append(ncol_i)

                col_i = list(map(int, file.readline().split()))
                if len(col_i) != ncol_i:
                    # throws an exception
                    pass
                col.append([x - 1 for x in col_i])

            # Info of rows that are covered by each column
            rows = [[] for _ in range(n)]
            nrow = [0] * n
            k = [0] * n

            for i in range(m):
                for h in range(ncol[i]):
                    nrow[col[i][h]] += 1

            for j in range(n):
                rows[j] = [0] * nrow[j]
                k[j] = 0

            for i in range(m):
                for h in range(ncol[i]):
                    rows[col[i][h]][k[col[i][h]]] = i
                    k[col[i][h]] += 1

        return [(rows[i], cost[i]) for i in range(len(rows))]

    def get_subets_and_costs(self):
        subs_and_costs = [(self.rows[i], self.cost[i]) for i in range(len(self.rows))]
        return subs_and_costs

    # def print_instance(self, level):
    #     print('************************************************')
    #     print(f'SCP INSTANCE {self.scp_file}')
    #     print()
    #     print('PROBLEM SIZE')
    #     print(f'm = {self.m}\t n = {self.n}')
    #     print()
    #
    #     if level >= 1:
    #         print('COLUMN COST')
    #         print(' '.join(map(str, self.cost)))
    #         print()
    #         print(f'NUMBER OF ELEMENTS COVERED BY SUBSET 1 is {self.nrow[0]}')
    #         print(' '.join(map(str, self.rows[0])))
    #         print(f'NUMBER OF SUBSETS COVERING ELEMENT 1 is {self.ncol[0]}')
    #         print(' '.join(map(str, self.col[0])))
    #         print()
    #     print('*************************************************\n')
