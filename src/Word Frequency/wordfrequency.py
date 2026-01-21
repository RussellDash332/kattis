from collections import*;n,k,m,*v=open(0).read().split();C=Counter(v)
for i in sorted([c for c in C if len(c)>=int(m)],key=lambda x:(-C[x],x))[:int(k)]:print(i,C[i])