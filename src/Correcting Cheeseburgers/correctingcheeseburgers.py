N,*A=map(int,open(0).read().split());A=tuple(A);B=tuple(range(1,N+1));D={}
if A==B:print(0);exit()
D[A]=[0,9];D[B]=[9,0];Q=[(A,0),(B,1)];G=tuple({B[j:i]+B[:k]+B[i:]+B[k:j]for i in range(N)for j in range(i+1)for k in range(j+1)});H=tuple({B[k:j]+B[i:]+B[:k]+B[j:i]for i in range(N)for j in range(i+1)for k in range(j+1)})
for u,v in Q:
 for p in(G,H)[v]:
  t=tuple(u[i-1]for i in p)
  if t not in D:D[t]=[9,9]
  if D[t][v]>D[u][v]+1:
   D[t][v]=D[u][v]+1;Q+=[(t,v)]
   if D[t][1-v]<9:print(sum(D[t]))<exit()