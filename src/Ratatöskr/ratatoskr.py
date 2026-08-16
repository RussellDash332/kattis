n,r,a,b,*s=map(int,open(0).read().split());G=[[]for _ in'.'*n];Z=n
for i in range(n-1):u,v=s[2*i:2*i+2];G[u:=u-1]+=[v:=v-1];G[v]+=[u]
for i in range(n):
 q=[i];d=[0]*n;d[i]=1
 for u in q:
  for v in G[u]:
   if d[v]<1:d[v]=d[u]+1;q+=[v]
 Z=min(Z,max(d)-(i+1in(a, b)))
print(Z)