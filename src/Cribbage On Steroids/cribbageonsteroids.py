from collections import*;c=Counter(a:=[' A23456789TJQK'.index(i)for i in open(0).read().split()[1:]]);z=sum(i*~-i for i in c.values());p=d=0
for i in range(1,14):
 if c[i]:p=(p or 1)*c[i];d+=1
 else:z+=p*d*(d>2);p=d=0
z+=p*d*(d>2);D=[1]+[0]*15
for i in a:
 i=min(i,10)
 for j in range(15-i,-1,-1):D[i+j]+=D[j]
print(z+2*D[15])