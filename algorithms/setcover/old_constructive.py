class Randomized:
    def __init__(self):
        self.uncovered_elements = None
        self.selected_sets = None

    def set_cover(self, elements, sets):
        self.selected_sets = []
        self.uncovered_elements = set(elements)

        while self.uncovered_elements:
            max_covered = 0
            selected_set = None
            for s in sets:
                covered = self.uncovered_elements.intersection(sets[s])
                if len(covered) > max_covered:
                    max_covered = len(covered)
                    selected_set = s

            if selected_set is not None:
                self.selected_sets.append(selected_set)
                self.uncovered_elements -= sets[selected_set]
            else:
                break

        return self.selected_sets


