from functools import*;I=lambda:[*map(int,input().split())];N,S=I();G=[[]for _ in'.'*N];V=[I()for _ in G]
for _ in'.'*~-N:a,b=I();G[a:=a-1]+=[b:=b-1];G[b]+=[a]
@cache
def F(r,p=-1):
 c,w=V[r];d=[0]+[-1]*S;e=[-1]*-~S
 if c<=S:e[c]=w
 for v in G[r]:
  if v!=p:
   x,y=F(v,r);m=[*map(max,zip(x,y))];f=[0]+[-1]*S;g=[-1]*-~S
   for i in range(S+1):
    for j in range(S+1-i):
     if~d[i]*~m[j]:f[i+j]=max(f[i+j],d[i]+m[j])
     if~e[i]*~x[j]:g[i+j]=max(g[i+j],e[i]+x[j])
   d,e=f,g
 return d,e
print(max(map(max,F(0))))