from algorithms.setcover.local_search import create_local_search_solution, generate_neighborhood, generate_neighborhood_2
from solution_evaluation import evaluate


def create_local_search_solution_grasp(subsets, current_solution):
    # ([([0, 1, 2], '3'), ([3, 4], '5'), ([3, 4], '5')], 13)
    improved = True
    current_evaluation = evaluate(current_solution)

    while improved:
        improved = False
        best_neighbor = None
        best_neighbor_evaluation = current_evaluation
        neighborhood = generate_neighborhood_2(current_solution)
        space_count = len(neighborhood)

        for neighbor in neighborhood:
            space_count -= 1
            neighbor_evaluation = evaluate(neighbor)
            if neighbor_evaluation < best_neighbor_evaluation:
                best_neighbor = neighbor
                best_neighbor_evaluation = evaluate(best_neighbor)

        if best_neighbor_evaluation < current_evaluation:
            current_evaluation = best_neighbor_evaluation
            improved = True

        if improved or space_count == 0:
            break

    return current_solution


def create_grasp_solution(subsets, inicial_solution, max_iterations=100):
    best_solution = None
    best_evaluation = float('inf')
    for _ in range(max_iterations):
        # candidate_solution = create_local_search_solution(subsets, inicial_solution, max_iterations)
        candidate_solution = create_local_search_solution_grasp(subsets, inicial_solution)
        candidate_solution = candidate_solution
        candidate_evaluation = evaluate(candidate_solution)

        if candidate_evaluation < best_evaluation:
            best_solution = candidate_solution
            best_evaluation = candidate_evaluation

    return best_solution, best_evaluation
