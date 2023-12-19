from algorithms.setcover.local_search import create_local_search_solution, evaluate


def create_grasp_solution(subsets, inicial_solution, max_iterations=100):
    best_solution = None
    best_evaluation = float('inf')
    for _ in range(max_iterations):
        candidate_solution = create_local_search_solution(subsets, inicial_solution, max_iterations)
        candidate_solution = candidate_solution[0]
        candidate_evaluation = evaluate(candidate_solution)

        if candidate_evaluation < best_evaluation:
            best_solution = candidate_solution
            best_evaluation = candidate_evaluation

    return best_solution, best_evaluation


