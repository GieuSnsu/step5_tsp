from distance import distance, total_distance

class Solver_mst:
    def __init__(self, cities):
        self.cities = cities

    def solve(self):
        visited = {}

        # add the shortest edge
        c0_min = None
        c1_min = None
        d_min = 1800
        dist = {}
        for c0 in range(len(self.cities)):
            dist[c0] = {}
            for c1 in range(len(self.cities)):
                if c0 == c1:
                    continue
                d = 0
                if c0 < c1:
                    d = distance(self.cities[c0], self.cities[c1])
                else:
                    d = dist[c1][c0]
                dist[c0][c1] = d
                if d < d_min:
                    d_min = d
                    c0_min = c0
                    c1_min = c1
                    visited = {c0: [c1], c1: [c0]}

        # keep adding shortest edges
        while len(visited) < len(self.cities):
            c0_min = None
            c1_min = None
            d_min = 1800
            for c0 in visited.keys():
                for c1, d in dist[c0].items():
                    if d < d_min and not c1 in visited:
                        c0_min = c0
                        c1_min = c1
                        d_min = d
            visited[c0_min].append(c1_min)
            visited[c1_min] = [c0_min]

        # make a tour
        tour = [0]
        stack = [0]
        while len(tour) < len(self.cities):
            incompleted = True
            for city in visited[stack[-1]]:
                if city not in tour:
                    tour.append(city)
                    stack.append(city)
                    incompleted = False
                    break
            if incompleted:
                stack.pop()

        return tour, total_distance(self.cities, tour)