import math
import random

from distance import distance
import solver_random
import solver_greedy
# import solver_exact
import solver_2opt

NUM_CITIES_LIST = [5, 8, 16, 64, 128, 512, 2048]
SOLVERS = [solver_random, # in the order of cities generated
           solver_greedy, # visit the closest cities next
        #    solver_exact,  # try all possible solutions O(n!)
           solver_2opt]

def generate_cities(num_cities, max_x=1600.0, max_y=900.0, seed=1):
    random.seed(seed)
    cities = []
    for i in range(num_cities):
        cities.append((random.uniform(0, max_x), random.uniform(0, max_y)))
    return cities

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def main():
    for i in range(len(NUM_CITIES_LIST)):
        cities = generate_cities(NUM_CITIES_LIST[i])
        print('Challenge' + str(i))
        for solver in SOLVERS:
            solver_name = solver.__name__.split('_')[1]
            tour = solver.solve(cities)
            path_length = sum(distance(cities[tour[i]], cities[tour[(i + 1) % len(cities)]]) for i in range(len(cities)))
            print(solver_name + ': ' + str(path_length))
        print()

if __name__ == '__main__':
    main()
