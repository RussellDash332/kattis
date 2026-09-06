N,M=map(int,input().split());G=[[]for _ in'.'*N];Z=[0]*N
for _ in'.'*M:a,b=map(int,input().split());a-=1;b-=1;G[a]+=[b];G[b]+=[a]
for i in range(N):
 if Z[i]<1:
  Q=[i]
  for u in Q:
   if Z[u]<1:
    T=[1]*4
    for v in G[u]:T[Z[v]]=0
    for j in range(1,4):
     if T[j]:Z[u]=j;break
    Q.extend(G[u])
print(*Z)