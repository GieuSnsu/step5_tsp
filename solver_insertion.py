from distance import distance

class Solver_insertion:
    def __init__(self, cities):
        self.cities = cities

    def solve(self):
        # initial subtour of the shortest path
        c1, c2 = 0, 1
        path_length = 1800
        for i in range(len(self.cities)):
            for j in range(i + 1, len(self.cities)):
                d = distance(self.cities[i], self.cities[j])
                if d < path_length:
                    c1, c2 = i, j
                    path_length = d * 2
        tour = [c1, c2]

        # initialise unvisited cities
        unvisited = set()
        for c in (set(range(len(self.cities))) - set(tour)):
            unvisited.add((c, distance(self.cities[c1], self.cities[c])))
        inserted = c2

        while unvisited:
            # find the city to insert next
            c_min = None
            d_min = 1800
            for c in unvisited.copy():
                d = distance(self.cities[inserted], self.cities[c[0]])
                if d < c[1]:
                    unvisited.remove(c)
                    unvisited.add((c[0], d))
                if min(d, c[1]) < d_min:
                    c_min = c[0]
                    d_min = min(d, c[1])
            unvisited.remove((c_min, d_min))

            # find the position to insert
            pos_min = None
            inc_min = 3600
            for pos in range(len(tour)):
                inc = (distance(self.cities[c_min], self.cities[tour[pos]]) +
                       distance(self.cities[c_min], self.cities[tour[(pos + 1) % len(tour)]]) -
                       distance(self.cities[tour[pos]], self.cities[tour[(pos + 1) % len(tour)]]))
                if inc < inc_min:
                    pos_min = pos + 1
                    inc_min = inc
            tour.insert(pos_min, c_min)
            path_length += inc_min

        return tour, path_length
