import random
import math
import numpy as np
import matplotlib.pyplot as plt

#no. of sites
n = 500

l=np.zeros(n,dtype=int)
for i in range(n):
    l[i]=i+1

#density
p=np.zeros(n,dtype=float)

noOfCycles=1000

alpha = 0.8
beta = 0.2
q=1

for k in range(n):
    print(k, "   k")
    site=np.zeros(l[k],dtype=int)
    sitesOccupied=[]
    noOfParticles=0

    # while noOfParticles!=int(l[k]/2):
    #     t=random.randint(0,l[k]-1)
    #     if site[t]!=1:
    #         site[t]=1
    #         noOfParticles+=1
    #         sitesOccupied.append(t)
    # print(site,"   site")
    # print(sitesOccupied,"  config")

    for d in range(noOfCycles):

        if (0 in sitesOccupied) == False:
            t = random.uniform(0, 1)
            # print("t1 = ", t)
            if t < alpha:
                site[0] = 1
                sitesOccupied.append(0)
                noOfParticles += 1
            # print(site,"  s1")
            # print(sitesOccupied,"  so1")

        nop = noOfParticles

        # for i in range(nop):
        r=0
        while r<nop:
            # print(r,"  r")
            i=random.randint(0,nop-1)
            # print(i," i")
            w = sitesOccupied[i]
            if w==l[k]:
                continue
            # print(w," w")
            if sitesOccupied[i]==(l[k]-1) :
                t=random.uniform(0,1)
                # print("t2 = ",t)
                if t<beta:
                    # sitesOccupied.remove(l[k]-1)
                    sitesOccupied[i]=l[k]# to keep the length of the list same
                    site[l[k]-1]=0
                    noOfParticles-=1
                # print(noOfParticles,"   noOfParticles2")
                # print(site,"  s2")
                # print(sitesOccupied,"  so2")

            elif site[sitesOccupied[i] +1]==0 :
                t=random.uniform(0,1)
                # print("t3 = ",t)
                if t<q:
                    sitesOccupied[i]=(w+1)
                    site[w]=0
                    site[w+1]=1
                # print(site, "  s3")
                # print(sitesOccupied, "  so3")
            r+=1

        sitesOccupied = [x for x in sitesOccupied if x != l[k]]
        # print(site,"  site r l[k]")
        # print(sitesOccupied," siteOccupied r l[k]")

    # print("nop                             ",noOfParticles)
    p[k]=noOfParticles/l[k]

# print(p,"     p")
# print(l,"    l")
plt.scatter(l,p,marker="o")
plt.xlabel("L(no. of sites)")
plt.ylabel("Density")
plt.show()

# in this i m selecting particles sequencially, so to how to bring a particle at site[0],
#  like i cannot choose site[0] if i m dealing with particles ?