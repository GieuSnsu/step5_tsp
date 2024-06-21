from solver_greedy import Solver_greedy
from solver_insertion import Solver_insertion
from distance import distance

class Solver_2opt:
    def __init__(self, cities, tour, path_length):
        self.cities = cities
        self.tour = tour
        self.path_length = path_length

    def direction(self, a, b, c):
        return (c[0] - a[0]) * (b[1] - a[1]) - (c[1] - a[1]) * (b[0] - a[0])

    def solve(self):
        updated = True
        while updated:
            updated = False
            for i in range(len(self.tour) - 2):
                for j in range(i + 2, len(self.tour) - 1):
                    c1 = self.cities[self.tour[i]]
                    c2 = self.cities[self.tour[i + 1]]
                    c3 = self.cities[self.tour[j]]
                    c4 = self.cities[self.tour[(j + 1) % len(self.tour)]]
                    d1 = self.direction(c3, c4, c1)
                    d2 = self.direction(c3, c4, c2)
                    d3 = self.direction(c1, c2, c3)
                    d4 = self.direction(c1, c2, c4)

                    # if i to (i + 1) and j to (j + 1) intersect
                    if (((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and
                        ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0))):
                        self.path_length -= distance(c1, c2)
                        self.path_length -= distance(c3, c4)
                        self.path_length += distance(c1, c3)
                        self.path_length += distance(c2, c4)
                        self.tour = (self.tour[: i + 1] +
                                     list(reversed(self.tour[i + 1 : j + 1])) +
                                     self.tour[j + 1 :])
                        updated = True

        return self.tour, self.path_length
