from algorithms.setcover.local_search import create_local_search_solution
from solution_evaluation import evaluate

import random


def generate_pertubation(candidate_solution):
    index1, index2 = random.sample(range(len(candidate_solution)), 2)
    candidate_solution[index1], candidate_solution[index2] = candidate_solution[index2], candidate_solution[index1]
    return candidate_solution

def create_iterated_local_search(inicial_solution, max_iterations=100):
    current_solution = inicial_solution
    candidate_solution = create_local_search_solution(inicial_solution, max_iterations)
    best_evaluation = evaluate(inicial_solution)
    for _ in range(max_iterations):
        pertubation = generate_pertubation(candidate_solution[0])
        candidate_solution = create_local_search_solution(pertubation, max_iterations=1)
        candidate_solution_ = candidate_solution[0]
        candidate_evaluation = evaluate(candidate_solution_)
        if candidate_evaluation < best_evaluation:
            best_solution = candidate_solution_
            best_evaluation = candidate_evaluation
            current_solution = best_solution

    return current_solution, candidate_evaluation
