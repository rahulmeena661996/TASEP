import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, a, b, c):
    return a * np.longfloat(np.exp(np.longfloat(-b * x))) + c

#no. of sites
n = 300

noOfCycles=1000

l=np.zeros(n,dtype=int)
for i in range(n):
    l[i]=i+1

#density
p=np.zeros(n,dtype=float)

alpha = 0.2
beta = 0.8
q=1
# remember to change error formula accordingly


for k in range(n):

    site = np.zeros(l[k],dtype=int)
    noOfParticles=0
    for r in range(noOfCycles):
        v=0
        while v < l[k]:
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
            elif i==l[k]-1 and site[l[k]-1]==1 :
                t= random.uniform(0,1)
                # print(t,"t2")
                if t<beta :
                    site[l[k]-1]=0
                    noOfParticles-=1
                # print(site , "2nd if")
                # print(noOfParticles,"no of 2")
            elif -1<i<(l[k]-1) and site[i]==1 and site[i+1]==0:
                t=random.uniform(0,1)
                # print(t, "t3")
                if t<q :
                    site[i]=0
                    site[i+1]=1
            v+=1
            # print(site , "3rd if")
            # print(noOfParticles,"no of 3")
        # print(r, "                     r")
    p[k]=noOfParticles/l[k]
    print(k)

#error stuff

# pa = a(1-a)/q-a^2, pb= (q-b)/(q-b^2), pc=0.5
pCorrect= np.full(n,alpha*(1-alpha)/(q-np.square(alpha)))
pCorrectS=alpha*(1-alpha)/(q-np.square(alpha))

meanP=np.mean(p)
errorPercentage=(meanP-pCorrectS)/pCorrectS*100

# error=np.zeros(n,dtype=float)

# for i in range(n):
#     error[i]=(p[i]-pCorrect[i])/pCorrect[i]*100
# print(error,"  error")
# print(np.mean(error)," mean error")
print(errorPercentage)
# standard dev.
# sigma=np.sqrt(np.mean(np.square(error))-np.square(np.mean(error)))
# print(sigma,"   sigma")
plt.scatter(l,pCorrect,color='red',marker='o')

# Fit for the parameters a, b, c of the function `func`

popt, pcov = curve_fit(func, l, p)
plt.plot(l, func(l, *popt), 'r-', label='fit')

# Constrain the optimization to the region of ``0 < a < 3``, ``0 < b < 2``
# and ``0 < c < 1``:

popt, pcov = curve_fit(func, l, p, bounds=(0, [0.5,0.5, 1.]))
plt.plot(l, func(l, *popt), 'g--', label='fit-with-bounds')



print(p)
plt.scatter(l,p,marker='o')
plt.xlabel("L(no. of sites)")
plt.ylabel("Density")
plt.show()





