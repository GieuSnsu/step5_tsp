import math
from distance import distance

def solve(cities):
    num_cities = len(cities)

    dist = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i, num_cities):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, num_cities))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour
