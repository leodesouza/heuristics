import os
import time
from algorithms.setcover.constructive import randomized_constructive, greedy_constructive, weighted_greedy_constructive, \
    redundancy_elimination
from algorithms.config import Parameters
from algorithms.utils.pseudo_random_generator import lecuyer_rando
from algorithms.setcover.local_search import create_local_search_solution
from algorithms.setcover.metaheuristics.grasp import create_grasp_solution
from algorithms.setcover.metaheuristics.iterated_local_search import create_iterated_local_search
from algorithms.setcover.metaheuristics.simulated_annealing import create_simulated_annealing


def write_to_file(instance_name, constructive_method_name, constructive_total_weight,
                  local_search, local_search_total_weigth,
                  metaheuristic, metaheuristic_total_weight, cpu_time, output_file):
    with open(output_file, 'a', newline='') as file:
        file.writelines(f'{instance_name};{constructive_method_name};{constructive_total_weight}'
                        f';{local_search};{local_search_total_weigth};{metaheuristic};{metaheuristic_total_weight};{cpu_time}\n')


class ScpV2:

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
                constructive_result = randomized_constructive.create_randomized_constructive(subsets,
                                                                                             pseudo_random_generated)
                constructive_total_weight = constructive_result[1]
            elif 'hc2' in parameters.options:
                constructive_method_name = 'HC2'
                constructive_result = greedy_constructive.create_greedy_constructive(subsets)
                constructive_total_weight = constructive_result[1]
            elif 'hc3' in parameters.options:
                constructive_method_name = 'HC3'
                constructive_result = weighted_greedy_constructive.create_wighted_greedy_constructive(subsets)
                constructive_total_weight = constructive_result[1]

            if 're' in parameters.options:
                constructive_result = redundancy_elimination.remove_rendundancy(constructive_result)

            local_search_method_name = 0
            local_search_total_weigth = 0
            if 'localsearch' in parameters.options:
                local_search_method_name = 1
                local_search_total_result = create_local_search_solution(subsets, constructive_result[0], 5)
                local_search_total_weigth = local_search_total_result[1]

            # --localsearch --grasp --itlocalsearch --sa
            metaheuristic_method_used = ''
            if 'grasp' in parameters.options:
                metaheuristic_method_used = 'GRASP'
                metaheuristic_results = create_grasp_solution(subsets, constructive_result[0], 5)
                metaheuristic_total_weight = metaheuristic_results[1]
            elif 'itlocalsearch' in parameters.options:
                metaheuristic_method_used = 'ILS'
                metaheuristic_results = create_iterated_local_search(subsets, constructive_result[0], 5)
                metaheuristic_total_weight = metaheuristic_results[1]
            elif 'sa' in parameters.options:
                metaheuristic_method_used = 'SA'
                metaheuristic_results = create_simulated_annealing(subsets, constructive_result[0], 5)
                metaheuristic_total_weight = metaheuristic_results[1]

            end_cpu_time = time.process_time()
            cpu_executation_time = (end_cpu_time - start_cpu_time)
            # ** End CPU Time **

            output_file = os.path.join(parameters.source, parameters.output_file)
            file_name, extension = os.path.splitext(file_name)

            write_to_file(file_name, constructive_method_name, constructive_total_weight, local_search_method_name,
                          local_search_total_weigth,
                          metaheuristic_method_used,
                          metaheuristic_total_weight,
                          cpu_executation_time,
                          output_file)

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

        return [(rows[i], cost[i]) for i in range(len(rows))]
