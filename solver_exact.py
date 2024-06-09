import itertools
from distance import distance

def solve(cities):
    all_tours = itertools.permutations(list(range(len(cities))))
    shortest_tour = []
    shortest_path = 2000 * len(cities)
    for tour in all_tours:
        path_length = 0
        path_length = sum(distance(cities[tour[i]], cities[tour[(i + 1) % len(cities)]]) for i in range(len(cities)))
        if path_length < shortest_path:
            shortest_tour = tour
            shortest_path = path_length
    return shortest_tour
