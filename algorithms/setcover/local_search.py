def evaluate(solution):
    # loop and update the total weight
    # covered = set()
    total_weight = 0
    for subset, weight in solution:
        # covered |= set(subset)
        total_weight += int(weight)

    return total_weight


def generate_neighborhood(subsets, solution):
    neighborhood = []
    for i, (subset, weight) in enumerate(solution):
        for j, (new_subset, new_weight) in enumerate(subsets):
            if j != i and not set(new_subset) - set(subset):
                new_solution = solution[:]
                new_solution[i] = (new_subset, new_weight)
                neighborhood.append(new_solution)

    return neighborhood


def create_local_search_solution(subsets, inicial_solution, max_iterations=1000):
    # ([([0, 1, 2], '3'), ([3, 4], '5'), ([3, 4], '5')], 13)
    current_solution = inicial_solution
    current_evaluation = evaluate(current_solution)
    iteration = 0
    try:
        while iteration < max_iterations:
            best_neighbor = None
            best_neighbor_evaluation = current_evaluation

            neighborhood = generate_neighborhood(subsets, current_solution)
            for neighbor in neighborhood:
                neighbor_evaluation = evaluate(neighbor)
                # if type(best_neighbor_evaluation) is list or type(neighbor_evaluation) is list:
                #     print("best_neighbor_evaluation", best_neighbor_evaluation)
                #     print("neighbor_evaluation", neighbor_evaluation)
                if neighbor_evaluation < best_neighbor_evaluation:
                    best_neighbor = neighbor
                    best_neighbor_evaluation = best_neighbor

            if best_neighbor_evaluation < current_evaluation:
                current_solution = best_neighbor
                current_evaluation = best_neighbor_evaluation
            else:
                break
            iteration += 1
    except BaseException as e:
        print("Error", e)

    return current_solution, current_evaluation

# max_iterations = 1000
# inicial_solution = []
# best_solution = local_search_weighted(inicial_solution, max_iterations=1000)
# evaluation = evaluate(best_solution)
# print(------)
