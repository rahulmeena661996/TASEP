import random
import math
import numpy as np
import matplotlib.pyplot as plt

#no. of sites
n = 1000

l=np.zeros(n,dtype=int)
for i in range(n):
    l[i]=i+1

#density
p=np.zeros(n,dtype=float)

alpha = 1
beta = 0
q=1

for k in range(n):

    site = np.zeros(l[k],dtype=int)
    noOfParticles=0
    sitesOccupied=[]
    for r in range(100):
        i = random.randint(0,l[k]-1)
        # print(i," i")
        if i==0 and site[0]==0 :
            t=random.uniform(0,1)
            # print(t,"t1")
            if t<alpha :
                site[0]=1
                noOfParticles+=1
            # print(site ,"1st if")
            # print(noOfParticles, "no of 1")
                sitesOccupied.append(0)

        elif i==l[k]-1 and site[l[k]-1]==1 :
            t= random.uniform(0,1)
            # print(t,"t2")
            if t<beta :
                site[l[k]-1]=0
                noOfParticles-=1
            # print(site , "2nd if")
            # print(noOfParticles,"no of 2")
                sitesOccupied.remove(l[k]-1)

        i=random.randint(0,len(sitesOccupied))
        if sitesOccupied[i] != l[k]-1 and site[sitesOccupied[i]+1]==0 :#elif i<l[k]-1 and i in sitesOccupied==True and (i+1) in sitesOccupied==False: #-1<i<(l[k]-1) and site[i]==1 and site[i+1]==0:
            t=random.uniform(0,1)
            # print(t, "t3")
            if t<q :
                site[i]=0
                site[i+1]=1
            # print(site , "3rd if")
            # print(noOfParticles,"no of 3")
        # print(r, "                     r")
                sitesOccupied.remove(i)
                sitesOccupied.append(i+1)
    p[k]=noOfParticles/l[k]
    print(k)
print(p)
plt.scatter(l,p,marker='o')
plt.xlabel("L(no. of sites)")
plt.ylabel("Density")
plt.show()

# if  i have to move particles randomly then how will i fill the first site.


