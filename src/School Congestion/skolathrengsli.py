I=input;n,m=map(int,I().split());g=[[]for _ in'.'*-~n];d=[-1]*-~n;q=[int(I())];d[q[0]]=0
for _ in'.'*m:a,b=map(int,I().split());g[b]+=[a]
for u in q:
 for v in g[u]:
  if d[v]<0:d[v]=d[u]+1;q+=[v]
for _ in'.'*int(I()):x=int(I());print(d[x]if~d[x]else"O nei!")