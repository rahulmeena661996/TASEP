import random
import math
import numpy as np
import matplotlib.pyplot as plt

#no. of sites
n = 25

l=np.zeros(n,dtype=int)
for i in range(n):
    l[i]=i+1

#density
p=np.zeros(n,dtype=float)

alpha = 0.5
beta = 0.5
q=0.5
"""
for a in range(n):
    # no. of particles
    noOfParticles=0
    site=np.zeros(a+1,dtype=int)
    if a==0:
        for r in range(100):
            if site[0]==0:
                t=random.uniform(0,1)
                if t<alpha:
                    site[0]=1
                    noOfParticles += 1
            else :
                t=random.uniform(0,1)
                if t<beta:
                    site[0]=0
                    noOfParticles -=1
        p[a] = noOfParticles / (a + 1)

    if a==1:
        for r in range(100):
            if site[0] == 0:
                t = random.uniform(0, 1)
                if t < alpha:
                    site[0] = 1
                    noOfParticles += 1

            if site[0]==1 and site[1]==0:
                t=random.uniform(0,1)
                if t<q:
                    site[1]=1
                    site[0]=0

            if site[a] == 1:
                t = random.uniform(0, 1)
                if t < beta:
                    site[a] = 0
                    noOfParticles -= 1

            i = random.randint(0, 1)
            if site[0] == 1 and site[1] == 0:
                t = random.uniform(0, 1)
                if t < q:
                    site[0] = 0
                    site[1] = 1
        p[a] = noOfParticles / (a + 1)


    if a>1 :
        for r in range(100):
            if site[0]==0 :
                t= random.uniform(0,1)
                if t<alpha:
                    site[0]=1
                    noOfParticles+=1

            i = random.randint(0, a - 1)
            if site[i] == 1 and site[i + 1] == 0:
                t = random.uniform(0, 1)
                if t < q:
                    site[i] = 0
                    site[i + 1] = 1

            if site[a]==1:
                t=random.uniform(0,1)
                if t<beta:
                    site[a]=0
                    noOfParticles-=1
        p[a]=noOfParticles/(a+1)
"""




for k in range(n):

    site = np.zeros(n,dtype=int)
    noOfParticles=0
    for r in range(1000):
        i = random.randint(0,n-1)
        print(i," i")
        if i==0 and site[0]==0 :
            t=random.uniform(0,1)
            print(t,"t1")
            if t<alpha :
                site[0]=1
                noOfParticles+=1
            print(site ,"1st if")
            print(noOfParticles, "no of 1")
        elif i==n-1 and site[n-1]==1 :
            t= random.uniform(0,1)
            print(t,"t2")
            if t<beta :
                site[n-1]=0
                noOfParticles-=1
            print(site , "2nd if")
            print(noOfParticles,"no of 2")
        elif -1<i<(n-1) and site[i]==1 and site[i+1]==0:
            t=random.uniform(0,1)
            print(t, "t3")
            if t<q :
                site[i]=0
                site[i+1]=1
            print(site , "3rd if")
            print(noOfParticles,"no of 3")
    p[k]=noOfParticles/l[k]
    print(r,"                     r")
print(p)
plt.scatter(l,p,marker='o')
plt.show()




