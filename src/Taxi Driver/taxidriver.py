from heapq import*
I=lambda:map(int,input().split());R,C,N=I();G=[[]for _ in'.'*R*C*4]
s,a,t,b=I();S=~-s*C+a-1;T=~-t*C+b-1;X=[(0,1),(-1,2),(1,3)];K=((0,1),(-1,0),(0,-1),(1,0));Z=[]
for _ in'.'*N:
 s,a,t,r,l=I();p=4*~-s*C+4*~-a
 for i in(0,1,2,3):G[p+i]=[(0,t),(-1,r),(1,l)]
for e in(0,3,*range(4*S,4*S+4),*range(4*T,4*T+4)):
 D=[1e9]*4*R*C;Q=[];D[e]=0;Q=[(0,e)]
 while Q:
  d,v=heappop(Q);p,i=divmod(v,4);r,c=divmod(p,C)
  if d-D[v]:continue
  for j,w in G[v]or X:
   a,b=K[(i+j)%4];w=w*(v>3)+1
   if R>r+a>-1<c+b<C and D[m:=4*(p+C*a+b)+(i+j)%4]>d+w:D[m]=d+w;heappush(Q,(d+w,m))
 Z+=[D]
print(min(Z[i][4*S+j-2]+Z[j][4*T+k-6]+Z[k][l]for i in(0,1)for j in(2,3,4,5)for k in(6,7,8,9)for l in(1,2)))