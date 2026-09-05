for _ in range(int(input())):
 n=int(input());g=[[]for _ in range(n)];q=[0];d=[0]+[n]*n
 for _ in range(n-1):a,b=map(int,input().split());g[a]+=[b];g[b]+=[a]
 for u in q:
  for v in g[u]:
   if d[v]==n:d[v]=d[u]+1;q+=[v]
 q=q[-1:];d=[n]*n;d[q[0]]=0
 for u in q:
  for v in g[u]:
   if d[v]==n:d[v]=d[u]+1;q+=[v]
 print(-~max(d)//2)