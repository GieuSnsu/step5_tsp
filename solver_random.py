class Solver_random:
    def __init__(self, cities):
        self.cities = cities

    def solve(self):
        return list(range(len(self.cities)))
