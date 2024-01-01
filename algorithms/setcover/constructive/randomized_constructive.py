from algorithms.utils.pseudo_random_generator import generate_rand_permutation


def create_randomized_constructive(subsets_and_costs, pseudo_random):
    elements = set()
    aux_elements = set()
    for subSet in subsets_and_costs:
        elements.update(subSet[0])
        aux_elements.update(subSet[0])
    elements = list(elements)

    shuffled_vector = iter(generate_rand_permutation(len(elements), pseudo_random))
    solution = []
    while len(aux_elements) > 0:
        random_index = next(shuffled_vector)
        current = elements[random_index]
        aux_elements.remove(current)
        subsets_that_cover_current = [subs for subs in subsets_and_costs if
                                      current in subs[0] and not any(e in solution for e in subs)]
        rand_permutation_of_subsets = generate_rand_permutation(len(subsets_that_cover_current), pseudo_random)
        index_of_first_subset = rand_permutation_of_subsets[0]
        local_solution = subsets_that_cover_current[index_of_first_subset]
        solution.append(local_solution)

    return solution, sum(int(sub[1]) for sub in solution)
