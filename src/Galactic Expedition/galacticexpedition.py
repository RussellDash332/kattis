from heapq import*;Q=lambda x:int(input(f'{x}\n'));n,d=map(int,input().split());P=[complex(*map(int,input().split()))for _ in'.'*n];W=[0]+[-1]*n
while 1:
 q=[(0,0)];D=[0]+[1e9]*n;p=[-1]*n;C=[]
 while q:
  d,u=heappop(q)
  if u and W[u]<0:l=u;break
  o=u;u=W[u]
  if d>D[o]or D[u]<D[o]:continue
  D[u]=D[o]
  for i in range(n):
   if(z:=D[u]+abs(P[u]-P[i]))<D[i]:D[i]=z;heappush(q,(z,i));p[i]=o
 c=l
 while c:C+=[c];c=p[c]
 for i in C[::-1]:
  if i+1==n:print(n);exit()
  j=Q(i+1)-1
 W[l]=j;W[j]=l
 for i in C+[0]:Q(W[i]+1)