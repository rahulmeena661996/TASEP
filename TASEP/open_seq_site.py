import random
import math
import numpy as np
import matplotlib.pyplot as plt

#no. of sites
n = 500

noOfCycles=1000

l=np.zeros(n,dtype=int)
for i in range(n):
    l[i]=i+1

#density
p=np.zeros(n,dtype=float)

alpha = 0.8
beta = 0.8
q=1




for k in range(n):

    site = np.zeros(l[k],dtype=int)
    # for i in range(int(n / 2)):
    #     y=random.randint(0,n-1)
    #     if site[y] !=1 :
    #         site[y]=1
    noOfParticles=0

    for r in range(noOfCycles):
        # print(i," i")
        i=0
        while i <(l[k]):
            t = random.uniform(0,1)
            if i==0 and site[0]==0 :
                # t=random.uniform(0,1)
                # print(t,"t1")
                if t<alpha :
                    site[0]=1
                    noOfParticles+=1
                # print(site ,"1st if")
                # print(noOfParticles, "no of 1")
            elif i==l[k]-1 and site[l[k]-1]==1 :
                # t= random.uniform(0,1)
                # print(t,"t2")
                if t<beta :
                    site[l[k]-1]=0
                    noOfParticles-=1
                # print(site , "2nd if")
                # print(noOfParticles,"no of 2")
            elif -1<i<(l[k]-1) and site[i]==1 and site[i+1]==0:
                # t=random.uniform(0,1)
                # print(t, "t3")
                if t<q :
                    site[i]=0
                    site[i+1]=1
                    i+=1
                # print(site , "3rd if")
                # print(noOfParticles,"no of 3")
            i+=1
    p[k]=noOfParticles/l[k]
    print(k)
# print(p)
plt.scatter(l,p,marker='o')
plt.xlabel("L(no. of sites)")
plt.ylabel("")
plt.ylabel("Density")
plt.show()




