from distance import distance, total_distance

class Solver_bitonic:
    def __init__(self, cities):
        self.cities = cities
        self.cities_info = sorted(list(enumerate(cities)),
                                  key=lambda city_info: city_info[1][0]) # + city_info[1][1])
        self.recursive_called = {}

    # Input  : [(original_index, (x, y))], index of the list, index of the list
    # Output : (distance, (original_index, original_index))
    def distance_and_path(self, city1, city2):
        d = distance(self.cities_info[city1][1], self.cities_info[city2][1])
        p = (min(self.cities_info[city1][0], self.cities_info[city2][0]),
             max(self.cities_info[city1][0], self.cities_info[city2][0]))
        return (d, p)

    # Input  : [(original_index, (x, y))]
    # Output : (path_length, [original_index])
    def recursive_bitonic(self, num_cities):
        if num_cities in self.recursive_called:
            ps, ds = self.recursive_called[num_cities]
            return (ps, ds.copy())
        
        if num_cities == 2:
            return (2 * distance(self.cities_info[0][1], self.cities_info[1][1]),
                    {(min(self.cities_info[0][0], self.cities_info[1][0]),
                      max(self.cities_info[0][0], self.cities_info[1][0]))})
        
        min_ds = 1800 * num_cities
        min_ps = None
        for i in range(1, num_cities - 1):
            # from city 0 to i (best paths)
            ds, ps = self.recursive_bitonic(i + 1)
            
            # from city i - 1 to i (direct)
            d, _ = self.distance_and_path(i - 1, i)
            ds += -d

            # from city i - 1 to n - 1 (direct)
            d, p = self.distance_and_path(i - 1, num_cities - 1)
            ds += d
            if i != 1:
                ps.add(p)

            # from city i to n - 2 (paths in order)
            for j in range(i, num_cities - 2):
                d, p = self.distance_and_path(j, j + 1)
                ds += d
                ps.add(p)
            
            # from city n - 2 to n - 1 (direct)
            d, p = self.distance_and_path(num_cities - 2, num_cities - 1)
            ds += d
            if num_cities == len(self.cities_info):
                ps.add(p)

            if ds < min_ds:
                min_ds = ds
                min_ps = ps
        self.recursive_called[num_cities] = (min_ds, min_ps.copy())
        return (min_ds, min_ps)

    def solve(self):
        ds, ps = self.recursive_bitonic(len(self.cities_info))
        tour = [self.cities_info[0][0]]
        while ps:
            for p in ps:
                if tour[-1] in p:
                    tour.append(p[1] if tour[-1] == p[0] else p[0])
                    ps.remove(p)
                    break
        return tour, ds
