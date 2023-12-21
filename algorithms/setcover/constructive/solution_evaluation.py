def evaluate(solution):
    # loop and update the total weight
    # covered = set()
    total_weight = 0
    if isinstance(solution, tuple):
        total_weight = int(solution[1])
        return total_weight

    for subset, weight in solution:
        # covered |= set(subset)
        total_weight += int(weight)

    return total_weight
