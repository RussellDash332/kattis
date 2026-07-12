import sys;input=sys.stdin.readline;I=lambda:map(int,input().split());N,M=I();G=[{}for _ in'.'*N];B=1e9;from heapq import*;Z=[]
for _ in'.'*M:a,b,w=I();G[a-1][b-1]=min(G[a-1].get(b-1,B),-w)
for s in range(N):
 D=[B]*N;D[s]=0;Q=[s]
 while Q:
  d,v=divmod(heappop(Q),N)
  if d-D[v]:continue
  for n,w in G[v].items():
   if D[n]>d+w:D[n]=d+w;heappush(Q,(d+w)*N+n)
 Z+=[D]
for _ in'.'*int(input()):s,t,k,*v=I();X=min(Z[s-1][x-1]+Z[x-1][t-1]for x in v);print(-X if X<1e8else'NO PATH')