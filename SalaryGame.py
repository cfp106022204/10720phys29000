import numpy as np
import matplotlib.pyplot as plt
n,m,k,dm=200,40,30,10
money=np.linspace(m,m,n)
for i in range(k):
    p1=p2=0
    while (p1==p2 or money[p1]==0 or money[p2]==0):
        p1=np.random.randint(0,n)
        p2=np.random.randint(0,n)
        
    win=np.random.randint(0,1)
    if win==0:
        money[p1]-=dm
        money[p2]+=dm
    else:
        money[p1]+=dm
        money[p2]-=dm

bins=10
plt.clf()
plt.hist(money,bins)
plt.ylim(0,n)
plt.show()