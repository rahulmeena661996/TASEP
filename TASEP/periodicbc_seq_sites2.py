#peridic_bc_seq_sites_2
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
n=10
q=0.2

noOfCycles=10000

#no. of particles
m = np.zeros(n+1,dtype=int)
for i in range(n+1):
    m[i]=i

j = np.zeros(n+1,dtype=float)



for g in range(n+1):
    # array for sites
    site = np.zeros(n, dtype=int)
    noOfParticles = 0
    #generating config
    while(noOfParticles!=m[g]):
        i=random.randint(0,n-1)
        if site[i] != 1:
            site[i]=1
            noOfParticles+=1
    print(site,"     config")


    for d in range(noOfCycles):
        #updating
        i=0
        while i <(n):
            if i<n-1 and site[i]==1 and site[i+1]==0:
                t=random.uniform(0,1)
                if t<q:
                    site[i]=0
                    site[i+1]=1
                    i+=1

            elif i==n-1 and site[n-1]==1 and site[0]==0 :
                t=random.uniform(0,1)
                if t<q:
                    site[0]=1
                    site[n-1]=0
                    j[g]+=1
            i+=1

    print(g)
plt.scatter(m/n,j/noOfCycles,marker='o')
plt.show()