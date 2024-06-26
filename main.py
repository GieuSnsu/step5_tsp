import random
import matplotlib.pyplot as plt

from distance import total_distance
from solver_random import Solver_random
from solver_greedy import Solver_greedy
# from solver_exact import Solver_exact
from solver_2opt import Solver_2opt
# from solver_bitonic import Solver_bitonic
from solver_insertion import Solver_insertion
from solver_mst import Solver_mst

NUM_CITIES_LIST = [8192]
# NUM_CITIES_LIST = [5, 8, 16, 64, 128, 512, 2048]
SOLVERS = [
           Solver_random,    # in the order of cities generated
        #    Solver_exact,     # try all possible solutions O(n!)
           Solver_greedy,    # visit the closest cities next
        #    Solver_bitonic,   # from the leftmost city, go to the rightmost, then come back
           Solver_insertion, # connect the shortest remaining path
           Solver_mst,       # build a minimum spanning tree, and visit them in the order
          ]

def generate_cities(num_cities, max_x=1600.0, max_y=900.0, seed=1):
    random.seed(seed)
    cities = []
    for i in range(num_cities):
        cities.append((random.uniform(0, max_x), random.uniform(0, max_y)))
    return cities

def main():
    for i in range(len(NUM_CITIES_LIST)):
        cities = generate_cities(NUM_CITIES_LIST[i])

        print('Challenge' + str(i))
        for solver in SOLVERS:
            solver_name = solver.__name__.split('_')[1]
            tour, path_length = solver(cities).solve()
            assert len(tour) == len(cities)
            print(solver_name + ': ' + str(path_length))

            # apply 2-opt
            tour, path_length = Solver_2opt(cities, tour, path_length).solve()
            assert len(tour) == len(cities)
            print(solver_name + "_2opt: " + str(path_length))

            # plot the graph
            xs, ys = zip(*[cities[i] for i in tour])
            plt.plot(xs, ys, marker='o')
            plt.show()

        print()

if __name__ == '__main__':
    main()
