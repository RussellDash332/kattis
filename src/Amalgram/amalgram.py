from collections import*;C=Counter
c=C()
for i in(0,1):
 d=C(input())
 for k in d:c[k]=max(c[k],d[k])
for i in c:print(i*c[i],end='')