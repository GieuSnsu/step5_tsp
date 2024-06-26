import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(cities, tour):
    return sum(distance(cities[tour[i]], cities[tour[(i + 1) % len(cities)]]) for i in range(len(cities)))