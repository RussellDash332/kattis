n,*a=map(int,open(0).read().split());I=[0]*-~n;Z=[*I]
for i in range(n):a[i]=a[i]-1if~a[i]else n;I[a[i]]+=1
Q=[i for i in range(n)if I[i]<1]
for u in Q:
 if u<n:v=a[u];I[v]-=1;Z[v]^=Z[u]+1;I[v]<1!=Q.append(v)
print(f'*{Z[n]}')