import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

# defining ncr, to be used later
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

#no. of sites
n = 100

#no. of particles
m = np.zeros(n+1,dtype=int)
for i in range(n+1):
    m[i] = i

noOfCycles=20

#flux
j = np.zeros(n+1,dtype=int)


# for diff values of m
for g in range(n+1):

    noofsitesOccupied = 0
    site = np.zeros(n,dtype=int)
    sitesOccupied = np.zeros(m[g],dtype=int)



    #probability of occupying next site
    q = 1
    #ji is array for value of j for diff. configs with same m[g]
    ji = np.zeros(ncr(n,m[g]),dtype=int)

    #trying all possible configs to remove bias
    for y in range(ncr(n,m[g])):

        #generating config
        while noofsitesOccupied != m[g] :
            i = random.randint(0,n-1)
            if site[i] != 1 :
                site[i]=1
                sitesOccupied[noofsitesOccupied] = i
                noofsitesOccupied+=1


        # print(site)
        # print(noofsitesOccupied)
        # print(sitesOccupied)
    # d here is the number of cycles
        for d in range(noOfCycles):
            #movement in one time period
            for b in range(m[g]):
                i = random.randint(0,m[g]-1)
                if sitesOccupied[i] != n-1 and site[sitesOccupied[i] +1] != 1 :
                    t = random.uniform(0,1)
                    if t<q :
                        site[sitesOccupied[i]]=0
                        site[sitesOccupied[i]+1]= 1


                if sitesOccupied[i] == n-1 and site[0] == 0:
                    w = random.uniform(0,1)
                    if w<q :
                        site[0] = 1
                        site[n-1] = 0
                        ji[y]+=1

                #updating sitesOccupied array
                r=0
                for z in range(n):
                    if site[z] == 1 :
                        sitesOccupied[r] = z
                        r+=1
    j[g] = np.mean(ji)


#plot of j vs density
plt.scatter(m/n,j/noOfCycles,marker='o')
plt.show()
# print(site)
# print(noofsitesOccupied)
# print(sitesOccupied)
print(j)




