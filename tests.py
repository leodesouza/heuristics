import random

array = [[0, 1, 2], [2, 3], [5, 6], [3, 4], [4, 5, 6], [0, 1, 3, 6]]


def randomized_constructive_heuristic(arr):
    solution = []
    for sublist in arr:
        if len(sublist) > 0:
            random_element = random.choice(sublist)
            solution.append(random_element)
    return solution


random_solution = randomized_constructive_heuristic(array)
print("Randomized Constructive Heuristic Solution:", random_solution)
