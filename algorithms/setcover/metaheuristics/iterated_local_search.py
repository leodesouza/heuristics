from algorithms.setcover.local_search import create_local_search_solution
from solution_evaluation import evaluate

import random


def generate_pertubation(candidate_solution):

    solucao_perturbada = candidate_solution
    _list = list(solucao_perturbada)[0]
    solucao_perturbada = _list
    if not isinstance(solucao_perturbada, tuple) and len(solucao_perturbada) >= 2:
        indice1 = random.randint(0, len(solucao_perturbada) - 2)
        indice2 = indice1 + 1
        # swap two adjacent elements, creating the double-bridge
        solucao_perturbada[indice1], solucao_perturbada[indice2] = solucao_perturbada[indice2], solucao_perturbada[
            indice1]
    return solucao_perturbada


def create_iterated_local_search(inicial_solution, max_iterations=100):
    current_solution = inicial_solution
    best_evaluation = float('inf')
    best_solution = []
    candidate_solution = create_local_search_solution(current_solution, max_iterations)
    for _ in range(max_iterations):
        # pertubation = generate_pertubation(candidate_solution)
        # pertubation = list(pertubation)
        # candidate_solution = create_local_search_solution(pertubation, max_iterations=1)
        candidate_solution = candidate_solution[0]
        if isinstance(candidate_solution, tuple):
            candidate_solution = tuple(list(candidate_solution))

        if all(isinstance(item, int) for item in candidate_solution):
            break;
        candidate_evaluation = evaluate(candidate_solution)
        if candidate_evaluation < best_evaluation:
            best_solution = candidate_solution
            best_evaluation = candidate_evaluation

    return best_solution, candidate_evaluation
