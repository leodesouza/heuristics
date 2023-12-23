import random

from algorithms.setcover.local_search import create_local_search_solution, generate_neighborhood, generate_neighborhood_2
from algorithms.utils.pseudo_random_generator import create_index
from solution_evaluation import evaluate


def create_local_search_solution_grasp(pseudo_random, current_solution):
    improved = False
    percentage = 10
    while not improved:
        # best_neighbor = None
        best_neighbor_evaluation = evaluate(current_solution)
        neighborhood = generate_neighborhood_2(current_solution)
        max_solutions = int((percentage / 100) * len(neighborhood))
        neighborhood = sorted(neighborhood, key=lambda x: x[0])
        neighborhood = neighborhood[:max_solutions]
        space_count = len(neighborhood)
        while space_count != 0:
            random_index = create_index(0, len(neighborhood) - 1, pseudo_random)
            neighbor = neighborhood[random_index]
            neighbor_evaluation = evaluate(neighbor)
            if neighbor_evaluation < best_neighbor_evaluation:
                best_neighbor = neighbor
                best_neighbor_evaluation = evaluate(best_neighbor)
                current_evaluation = best_neighbor_evaluation
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
        # candidate_solution = create_local_search_solution(subsets, inicial_solution, max_iterations)
        candidate_solution = create_local_search_solution_grasp(pseudo_random, inicial_solution)
        candidate_solution = candidate_solution
        candidate_evaluation = evaluate(candidate_solution)

        if candidate_evaluation < best_evaluation:
            best_solution = candidate_solution
            best_evaluation = candidate_evaluation

    return best_solution, best_evaluation
