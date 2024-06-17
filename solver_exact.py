import itertools
from distance import total_distance

class Solver_exact:
    def __init__(self, cities):
        self.cities = cities

    def solve(self):
        all_tours = itertools.permutations(list(range(len(self.cities))))
        shortest_tour = []
        shortest_path = 1800 * len(self.cities)
        for tour in all_tours:
            path_length = 0
            path_length = total_distance(self.cities, tour)
            if path_length < shortest_path:
                shortest_tour = tour
                shortest_path = path_length
        return shortest_tour, shortest_path
