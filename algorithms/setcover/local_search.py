from redundancy_elimination import remove_rendundancy
from solution_evaluation import evaluate


def generate_neighborhood_2(solution):
    neighborhood = []

    for sublist_index, sublist in enumerate(solution):
        elements = sublist[0]  # Extracting elements from the sublist
        label = sublist[1]  # Extracting the label
        for i in range(len(elements)):
            for j in range(i + 1, len(elements)):
                new_elements = elements[:]  # Create a copy of the elements
                # Swap elements within the same sublist
                new_elements[i], new_elements[j] = new_elements[j], new_elements[i]
                new_solution = solution[:]  # Create a copy of the solution
                new_solution[sublist_index] = (new_elements, label)  # Update the sublist in the solution
                neighborhood.append(new_solution)  # Add to the neighborhood

    return neighborhood


def generate_neighborhood(subsets, solution):
    # neighborhood = []
    # ordered = sorted(subsets, key=lambda x: len(x[0]), reverse=True)
    # neighborhood.append(ordered)
    # return neighborhood

    neighborhood = []
    for i, (subset, weight) in enumerate(solution):
        for j, (new_subset, new_weight) in enumerate(subsets):
            if j != i and not set(new_subset) - set(subset):
                new_solution = solution[:]
                new_solution[i] = (new_subset, new_weight)
                neighborhood.append(new_solution)

    return neighborhood


def create_local_search_solution(inicial_solution, max_iterations=1000):
    # ([([0, 1, 2], '3'), ([3, 4], '5'), ([3, 4], '5')], 13)
    current_solution = inicial_solution
    current_evaluation = evaluate(current_solution)
    iteration = 0
    try:
        while iteration < max_iterations:
            best_neighbor = None
            best_neighbor_evaluation = current_evaluation
            neighborhood = generate_neighborhood_2(current_solution)
            for neighbor in neighborhood:
                neighbor_evaluation = evaluate(neighbor)
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

    # ([([0, 1, 2], '3'), ([3, 4], '5'), ([3, 4], '5')], 13)
    current_solution, current_evaluation = remove_rendundancy((current_solution, 0))

    return current_solution, current_evaluation
