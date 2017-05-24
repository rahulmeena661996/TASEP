import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

# defining ncr, to be used later
import operator as op


def ncr(n, r):
    r = min(r, n - r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n - r, -1))
    denom = reduce(op.mul, range(1, r + 1))
    return numer // denom


# no. of sites
n = 10

# no. of particles
m = np.zeros(n + 1, dtype=int)
for i in range(n + 1):
    m[i] = i

noOfCycles = 10

# flux
j = np.zeros(n + 1, dtype=int)

# for diff values of m
for g in range(n + 1):

    noofsitesOccupied = 0
    site = np.zeros(n, dtype=int)
    sitesOccupied = np.zeros(m[g], dtype=int)

    # probability of occupying next site
    q = 0.8
    # ji is array for value of j for diff. configs with same m[g]
    # ji = np.zeros(ncr(n, m[g]), dtype=int)

    # trying all possible configs to remove bias
    # for y in range(ncr(n,m[g])):

    # generating config
    while noofsitesOccupied != m[g]:
        i = random.randint(0, n - 1)
        if site[i] != 1:
            site[i] = 1
            sitesOccupied[noofsitesOccupied] = i
            noofsitesOccupied += 1
    print(site,"  config")
    print(sitesOccupied,"  sitesOccupied")

            # print(site)
            # print(noofsitesOccupied)
            # print(sitesOccupied)
            # d here is the number of cycles
    for d in range(noOfCycles):
        # movement in one time period
        for i in range(m[g]):
            # i = random.randint(0,m[g]-1)
            if sitesOccupied[i] != n - 1  and site[sitesOccupied[i] + 1] == 0:
                t = random.uniform(0, 1)
                print(t)
                if t < q:
                    site[sitesOccupied[i]] = 0
                    site[sitesOccupied[i] + 1] = 1
                print(site,"site1  ","i= ",i)
                print(sitesOccupied,"sitesOccupied1")

            elif sitesOccupied[i] == n - 1 and site[0] == 0:
                w = random.uniform(0, 1)
                print(w)
                if w < q:
                    site[0] = 1
                    site[n - 1] = 0
                    j[g] += 1
                print(site, "site2  ","i= ",i)
                print(sitesOccupied, "sitesOccupied2")

            # updating sitesOccupied array
            r = 0
            for z in range(n):
                if site[z] == 1:
                    sitesOccupied[r] = z
                    r += 1
            print(sitesOccupied,"  updated siteOccupied")
                    # j[g] = np.mean(ji)  # plot of j vs density
    print(g,"  g")
plt.scatter(m / n, j / noOfCycles, marker='o')
print(j)
plt.show()
# print(site)
# print(noofsitesOccupied)
# print(sitesOccupied)

