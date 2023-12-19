from algorithms.setcover.local_search import evaluate, create_local_search_solution


def create_iterated_local_search(subsets, inicial_solution, max_iterations=100):
    current_solution = inicial_solution
    best_evaluation = float('inf')
    best_solution = []
    for _ in range(max_iterations):
        candidate_solution = create_local_search_solution(subsets, current_solution, max_iterations)
        candidate_solution = candidate_solution[0]
        candidate_evaluation = evaluate(candidate_solution)
        if candidate_evaluation < best_evaluation:
            best_solution = candidate_solution
            best_evaluation = candidate_evaluation

    return best_solution, candidate_evaluation


