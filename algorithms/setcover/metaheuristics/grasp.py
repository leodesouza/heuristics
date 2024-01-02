import random

from algorithms.setcover.local_search import create_local_search_solution, generate_neighborhood, \
    generate_neighborhood_2
from algorithms.utils.pseudo_random_generator import create_index
from redundancy_elimination import remove_rendundancy
from solution_evaluation import evaluate


def check_all_elements_coverage(subsets, current_solution):
    covered_elements = set()
    current_elements = set()
    for s in subsets:
        covered_elements.update(s[0])
    for s in current_solution:
        current_elements.update(s[0])

    return covered_elements == current_elements


def create_local_search_solution_grasp(pseudo_random, current_solution):
    improved = False
    percentage = 10
    while not improved:
        # best_neighbor = None
        best_neighbor_evaluation = evaluate(current_solution)
        neighborhood = generate_neighborhood_2(current_solution)
        max_solutions = int((100 / percentage) * len(neighborhood))
        if max_solutions == 0:
            max_solutions = 1
        neighborhood = sorted(neighborhood, key=lambda x: x[0])
        neighborhood = neighborhood[:max_solutions]
        space_count = len(neighborhood)
        iter_neighborhood = iter(neighborhood)
        while space_count != 0:
            neighbor = next(iter_neighborhood)
            if check_all_elements_coverage(neighbor, current_solution):
                neighbor_evaluation = evaluate(neighbor)
                if neighbor_evaluation < best_neighbor_evaluation:
                    best_neighbor = neighbor
                    best_neighbor_evaluation = evaluate(best_neighbor)
                    current_solution = neighbor
                    improved = True
            space_count -= 1

        if space_count == 0:
            break

    return current_solution


def create_grasp_solution(subsets, inicial_solution, pseudo_random, max_iterations=100):
    best_solution = None
    best_evaluation = float('inf')

    for _ in range(max_iterations):
        candidate_solution = create_local_search_solution_grasp(pseudo_random, inicial_solution)
        candidate_solution = candidate_solution
        candidate_evaluation = evaluate(candidate_solution)
        if candidate_evaluation < best_evaluation:
            best_solution = candidate_solution
            best_evaluation = candidate_evaluation
            break

    return best_solution, best_evaluation
