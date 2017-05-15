import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

#no. of sites
n = 10

# particles
m = np.zeros(n+1,dtype=int)
for i in range(n+1):
    m[i] = i

noOfCycles = 10

q=0.5

#flux

j = np.zeros(n+1,dtype=int)

#noofsitesOccupied = 0
#site = np.zeros(n,dtype=int)
#sitesOccupied = np.zeros(m[g],dtype=int)

for g in range(n+1):

    noofsitesOccupied = 0
    site = np.zeros(n,dtype=int)
    #sitesOccupied = np.zeros(m[g],dtype=int)



    #probability of occupying next site
    q = 1
    #ji is array for value of j for diff. configs with same m[g]
    ji = np.zeros(ncr(n,m[g]),dtype=int)

    for y in range(ncr(n,m[g])):

        # generating config
        while noofsitesOccupied != m[g]:
            i = random.randint(0, n - 1)
            if site[i] != 1:
                site[i] = 1
                #sitesOccupied[noofsitesOccupied] = i
                noofsitesOccupied += 1
        print(site,"    config")

        for d in range(noOfCycles):
            #one loop
            for i in range(n):
                if i != n-1 and site[i]==1 and site[i+1]==0  :
                    t=random.uniform(0,1)
                    if t<q:
                        site[i]=0
                        site[i+1]=1
                        print(t,"  t1")
                    print(site,"  s1")
                elif i==n-1 and site[i]==1 and site[0]==0 :
                    t=random.uniform(0,1)
                    if t<q :
                        site[i]=0
                        site[0]=1
                        ji[y] += 1
                        print(t, "  t2")
                    print(site, "  s2")
    j[g] = np.mean(ji)
print(j)
plt.scatter(m/n,j/noOfCycles,marker='o')
plt.show()
