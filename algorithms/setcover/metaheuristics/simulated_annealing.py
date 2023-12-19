import math
import random

from algorithms.setcover.local_search import evaluate


def generate_neighborhood(subsets, solution):
    neighborhood = []
    for i, (subset, weight) in enumerate(solution):
        for j, (new_subset, new_weight) in enumerate(subsets):
            if j != i and not set(new_subset) - set(subset):
                new_solution = solution[:]
                new_solution[i] = (new_subset, new_weight)
                neighborhood.append(new_solution)

    return neighborhood


def create_simulated_annealing(subsets, inicial_solution,
                               initial_temperature=1000,
                               cooling_rate=0.99,
                               stopping_temperature=0.1):
    current_solution = inicial_solution
    temperature = initial_temperature
    while temperature > stopping_temperature:
        new_solution = generate_neighborhood(subsets, current_solution)[0]
        current_weight = evaluate(current_solution)
        new_weight = evaluate(new_solution)

        if new_weight < current_weight or random.uniform(0, 1) < math.exp((current_weight - new_weight) / temperature):
            current_solution = new_solution
        temperature *= cooling_rate
        current_weight = evaluate(current_solution)
    return current_solution, current_weight
