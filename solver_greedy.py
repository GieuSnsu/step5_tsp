from distance import distance

class Solver_greedy:
    def __init__(self, cities):
        self.cities = cities

    def solve(self):
        num_cities = len(self.cities)

        dist = [[0] * num_cities for _ in range(num_cities)]
        for i in range(num_cities):
            for j in range(i, num_cities):
                dist[i][j] = dist[j][i] = distance(self.cities[i], self.cities[j])

        current_city = 0
        unvisited = set(range(1, num_cities))
        tour = [current_city]
        path_length = 0

        while unvisited:
            next_city = min(unvisited, key=lambda city: dist[current_city][city])
            unvisited.remove(next_city)
            tour.append(next_city)
            path_length += dist[current_city][next_city]
            current_city = next_city
        
        path_length += dist[current_city][0]
        return tour, path_length
