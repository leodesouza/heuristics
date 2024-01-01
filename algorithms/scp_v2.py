import os
import time
from algorithms.setcover.constructive import randomized_constructive, greedy_constructive, \
    weighted_greedy_constructive, redundancy_elimination
from algorithms.utils.pseudo_random_generator import lecuyer_rando
from algorithms.setcover.metaheuristics.grasp import create_grasp_solution
from algorithms.setcover.metaheuristics.iterated_local_search import create_iterated_local_search
from algorithms.setcover.metaheuristics.simulated_annealing import create_simulated_annealing


def write_to_file(instance_name, m, n, best, hc1_weight, hc1_re, mh1_weight,
                  hc2_weight, hc2_re, mh2_weight, hc3_weight, hc3_re, mh3_weight, cpu_time, output_file):
    with open(output_file, 'a', newline='') as file:
        file.writelines(f'{instance_name};{m};{n};{best};{hc1_weight}'
                        f';{hc1_re};{mh1_weight};{hc2_weight};{hc2_re};{mh2_weight};'
                        f'{hc3_weight};{hc3_re};{mh3_weight};{cpu_time}\n')


class ScpV2:

    def process_instances(self, parameters, _max_experiments_iteration):

        files = os.listdir(parameters.source)
        already_wrote_head = False
        for file_name in files:
            if file_name == parameters.output_file:
                continue

            m = 0  # elements
            n = 0  # subsets
            file_path = os.path.join(parameters.source, file_name)
            m, n, subsets = self.get_subsets(file_path)
            pseudo_random = lecuyer_rando(parameters.seed)

            # ** Start CPU Time **
            start_cpu_time = time.process_time()
            hc1_re = 0
            hc2_re = 0
            hc3_re = 0

            if 'hc1' in parameters.options:
                constructive_result_1 = randomized_constructive.create_randomized_constructive(subsets, pseudo_random)
                hc1_weight = constructive_result_1[1]
            if 'hc2' in parameters.options:
                constructive_result_2 = greedy_constructive.create_greedy_constructive(subsets)
                hc2_weight = constructive_result_2[1]

            if 'hc3' in parameters.options:
                constructive_result_3 = weighted_greedy_constructive.create_wighted_greedy_constructive(subsets)
                hc3_weight = constructive_result_3[1]

            if 're' in parameters.options:
                constructive_result_1 = redundancy_elimination.remove_rendundancy(constructive_result_1)
                hc1_re = constructive_result_1[1]
                constructive_result_2 = redundancy_elimination.remove_rendundancy(constructive_result_2)
                hc2_re = constructive_result_2[1]
                constructive_result_3 = redundancy_elimination.remove_rendundancy(constructive_result_3)
                hc3_re = constructive_result_3[1]

            metaheuristic_method_used = ''
            if 'grasp' in parameters.options:
                metaheuristic_method_used = 'GRASP'
                # metaheuristic_results = create_grasp_solution(subsets, constructive_result[0], 5)
                # metaheuristic_total_weight = metaheuristic_results[1]

                result1 = create_grasp_solution(subsets, constructive_result_1[0], pseudo_random,
                                                _max_experiments_iteration)
                result2 = create_grasp_solution(subsets, constructive_result_2[0], pseudo_random,
                                                _max_experiments_iteration)
                result3 = create_grasp_solution(subsets, constructive_result_3[0], pseudo_random,
                                                _max_experiments_iteration)
                mh1_weight = result1[1]
                mh2_weight = result2[1]
                mh3_weight = result3[1]
            elif 'itlocalsearch' in parameters.options:
                metaheuristic_method_used = 'ILS'
                result1 = create_iterated_local_search(constructive_result_1[0], _max_experiments_iteration)
                result2 = create_iterated_local_search(constructive_result_2[0], _max_experiments_iteration)
                result3 = create_iterated_local_search(constructive_result_3[0], _max_experiments_iteration)
                mh1_weight = result1[1]
                mh2_weight = result2[1]
                mh3_weight = result3[1]

            elif 'sa' in parameters.options:
                metaheuristic_method_used = 'SA'
                result1 = create_simulated_annealing(subsets, constructive_result_1[0], _max_experiments_iteration)
                result2 = create_simulated_annealing(subsets, constructive_result_2[0], _max_experiments_iteration)
                result3 = create_simulated_annealing(subsets, constructive_result_3[0], _max_experiments_iteration)
                mh1_weight = result1[1]
                mh2_weight = result2[1]
                mh3_weight = result3[1]

            end_cpu_time = time.process_time()
            cpu_executation_time = round((end_cpu_time - start_cpu_time) / 1.0, 1) * 1000

            # ** End CPU Time **

            output_file = os.path.join(parameters.source, parameters.output_file)
            file_name, extension = os.path.splitext(file_name)
            if not already_wrote_head:
                write_to_file('Inst.', 'm', 'n', 'Best', 'HC1', '+ER1',
                              f'{metaheuristic_method_used}1',
                              'HC2', '+ER2',
                              f'{metaheuristic_method_used}2',
                              'HC3', '+ER3',
                              f'{metaheuristic_method_used}3',
                              'TEMPO(ms)', output_file)
                already_wrote_head = True

            best_value = 0
            write_to_file(file_name, m, n, best_value, hc1_weight, hc1_re, mh1_weight,
                          hc2_weight, hc2_re, mh2_weight,
                          hc3_weight, hc3_re, mh3_weight,
                          cpu_executation_time, output_file)

    @staticmethod
    def get_subsets(scp_file):
        try:
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

                m = rows_columns_number[0]  # number of elements
                n = rows_columns_number[1]  # number of subsets

                # reading all costs
                has_read_all_costs = False
                number_subets_that_cover_element = 0
                while not has_read_all_costs:
                    items = file.readline().split()
                    if len(items) == 1:
                        has_read_all_costs = True
                        number_subets_that_cover_element = items[0]
                        continue
                    cost.extend(items)

                # reading all subsets
                number_subets_that_cover_element = int(number_subets_that_cover_element)
                ncol.append(number_subets_that_cover_element)
                has_read_all_subsets = False
                count_read = 1
                col.append([])
                aux = []
                while count_read < m:
                    line = file.readline()
                    if not line:
                        break
                    inline_subsets = line.split()

                    for subset in inline_subsets:
                        if len(col[-1]) < number_subets_that_cover_element:
                            col[-1].append(int(subset) - 1)
                        else:
                            # [subs for subs in subsets_and_costs if current in subs[0]]
                            # jj = [x for x in subset if x not in col]
                            number_subets_that_cover_element = int(subset)
                            ncol.append(number_subets_that_cover_element)
                            col.append([])

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
        except BaseException as e:
            print(f'Error:{scp_file}')
            print(e)

        return m, n, [(rows[i], cost[i]) for i in range(len(rows))]
