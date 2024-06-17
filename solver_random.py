from distance import total_distance

class Solver_random:
    def __init__(self, cities):
        self.cities = cities
        self.tour = list(range(len(cities)))

    def solve(self):
        return (self.tour, total_distance(self.cities, self.tour))
