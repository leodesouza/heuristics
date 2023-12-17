
def create_greedy_constructive(subsets_and_costs):
    elements = set()
    for subSet in subsets_and_costs:
        elements.update(subSet[0])

    number_elements = len(list(elements))
    number_of_covered = 0
    solution = []
    ordered_subsets = iter(sorted(subsets_and_costs, key=lambda x: x[1]))

    while number_of_covered < number_elements:
        current_subset = next(ordered_subsets)
        for element in current_subset[0]:
            found = any(element in sublist for sublist in solution)
            if not found:
                number_of_covered += 1

        solution.append(current_subset)

    return solution, sum(sub[1] for sub in solution)
