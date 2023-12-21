from solution_evaluation import evaluate


def remove_rendundancy(solution):
    element_to_subset = {}
    solution = solution[0]
    sorted_solution = sorted(solution, key=lambda x: x[1])
    non_redundant_solution_2 = []

    for subset, weight in sorted_solution:
        already_covered = any(element in element_to_subset for element in subset)
        if not already_covered:
            non_redundant_solution_2.append((subset, weight))
            for element in subset:
                element_to_subset[element] = subset

    total_weight = evaluate(non_redundant_solution_2)
    return non_redundant_solution_2, total_weight
