import random
import math
import numpy as np
import matplotlib.pyplot as plt

#no. of sites
n = 10

#no. of particles
#m = 9
m = np.zeros(n+1,dtype=int)
for i in range(n+1):
    m[i] = i

#flux
j = np.zeros(n+1,dtype=int)


# for diff values of m
for g in range(n+1):

    noofsitesOccupied = 0
    site = np.zeros(n,dtype=int)
    sitesOccupied = np.zeros(m[g],dtype=int)

    #density = m/n

    #probability of occupying next site
    q = 1

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
    for d in range(10000):
        #movement in one time period
        for b in range(m[g]):
            i = random.randint(0,m[g]-1)
            if sitesOccupied[i] != n-1 and site[sitesOccupied[i] +1] != 1 :
                t = random.uniform(0,1)
                if t<q :
                    site[sitesOccupied[i]]=0
                    site[sitesOccupied[i]+1]= 1
                    #sitesOccupied[i] = sitesOccupied[i] +1

            if sitesOccupied[i] == n-1 and site[0] == 0:
                w = random.uniform(0,1)
                if w<q :
                    site[0] = 1
                    site[n-1] = 0
                    j[g]+=1
                    #print(2)
                    #sitesOccupied[i] = 0
            #updating sitesOccupied array
            r=0
            for z in range(n):
                if site[z] == 1 :
                    sitesOccupied[r] = z
                    r+=1

#plot of j vs density
plt.scatter(m/n,j/10000,marker='o')
plt.show()
# print(site)
# print(noofsitesOccupied)
# print(sitesOccupied)
print(j)




