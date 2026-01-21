import sys;from heapq import*;I=sys.stdin.readline;m,q=map(int,I().split());Q=[];H={};Z=lambda:P('error')<exit();P=print
for _ in'.'*q:
 c,*v=I().split()
 if'B'>c:
  x,k=map(int,v)
  if x in H:Z()
  H[x]=k;heappush(Q,k*m+x)
 elif'D'>c:
  x,k=map(int,v)
  if x not in H:Z()
  H[x]=k;heappush(Q,k*m+x)
 elif'F'>c:
  while Q:
   v=Q[0]
   if v%m not in H or H[v%m]-v//m:heappop(Q)
   else:break
  if not Q:Z()
  P(Q[0]%m)
 elif'H'>c:
  x=int(v[0])
  if x not in H:Z()
  P(H[x])
 elif'Q'>c:
  while Q:
   v=Q[0]
   if v%m not in H or H[v%m]-v//m:heappop(Q)
   else:break
  if not Q:Z()
  P(x:=heappop(Q)%m);del H[x]
 elif'S'>c:
  x=int(v[0])
  if x not in H:Z()
  del H[x]
 else:P(len(H))