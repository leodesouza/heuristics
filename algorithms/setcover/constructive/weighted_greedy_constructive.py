def create_wighted_greedy_constructive(subsets_and_costs):
    elements = set()
    for subSet in subsets_and_costs:
        elements.update(subSet[0])

    number_elements = len(list(elements))
    number_of_covered = 0
    solution = []
    lower_cost = 0
    # cover_cost = 0
    subsets_cost_per_cover = []
    for sub in subsets_and_costs:
        lower_number = min(len(sub[0]), sub[1])
        bigger_number = max(len(sub[0]), sub[1])
        cover_cost = bigger_number / lower_number
        subsets_cost_per_cover.append((sub[0], cover_cost))

    subsets_cost_per_cover = iter(sorted(subsets_cost_per_cover, key=lambda x: x[1]))

    while number_of_covered < number_elements:
        current_subset = next(subsets_cost_per_cover)
        for element in current_subset[0]:
            found = any(element in sublist for sublist in solution)
            if not found:
                number_of_covered += 1

        solution.append((current_subset[0], int(len(current_subset[0]) * current_subset[1])))

    return solution, sum(sub[1] for sub in solution)
