import solver_greedy

def direction(a, b, c):
    return (c[0] - a[0]) * (b[1] - a[1]) - (c[1] - a[1]) * (b[0] - a[0])

def solve(cities):
    tour = solver_greedy.solve(cities)
    for i in range(len(tour) - 2):
        c1 = cities[tour[i]]
        c2= cities[tour[i + 1]]
        for j in range(i + 2, len(tour)):
            c3 = cities[tour[j]]
            c4 = cities[tour[(j + 1) % len(tour)]]
            d1 = direction(c3, c4, c1)
            d2 = direction(c3, c4, c2)
            d3 = direction(c1, c2, c3)
            d4 = direction(c1, c2, c4)
            if (((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and
                ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0))):
                tour = (tour[: i + 1] +
                        list(reversed(tour[i + 1 : j + 1])) +
                        tour[j + 1 :])
    return tour
