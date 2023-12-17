from algorithms.utils.pseudo_random_generator import generate_rand_permutation


def create_randomized_constructive(subsets_and_costs, pseudo_random):
    elements = set()
    for subSet in subsets_and_costs:
        elements.update(subSet[0])
    elements = list(elements)

    shuffled_vector = iter(generate_rand_permutation(len(elements), pseudo_random))
    number_of_covered = 0
    solution = []
    number_elements = len(elements)

    while number_of_covered < number_elements:
        random_index = next(shuffled_vector)
        current = elements[random_index]
        subsets_that_cover_current = [subs for subs in subsets_and_costs if current in subs[0]]
        rand_permutation_of_subsets = generate_rand_permutation(len(subsets_that_cover_current), pseudo_random)
        index_of_first_subset = rand_permutation_of_subsets[0]
        # local_solution variable is not relate to local search algorithm
        local_solution = subsets_that_cover_current[index_of_first_subset]
        number_of_covered += 1
        for e in local_solution:
            if e != current:
                found = any(e in sublist for sublist in solution)
                if not found:
                    number_of_covered += 1
        solution.append(local_solution)

    return solution, sum(sub[1] for sub in solution)
