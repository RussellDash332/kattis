def T(l):
 if V[l]<1:
  V[l]=1
  for r in G[l]:
   if 0>M[r]or T(M[r]):M[r]=l;return 1
from cmath import*;N=int(input());P,Q=[[complex(*map(float,input().split()))for _ in'.'*N]for _ in'..'];L=0;H=pi
for _ in'.'*67:
 a=(L+H)/2;M=[-1]*2*N;F={*range(N)};G=[[j+N for j in range(N)if-a<=2*phase(Q[j]-P[i])-pi<=a]for i in range(N)]+[[]]*N
 for l in range(N):
  if(C:=[r for r in G[l] if M[r]<0]):F-={l};M[C[0]]=l
 for f in F:V=[0]*N;T(f)
 if~min(M[N:]):H=a
 else:L=a
print(a*180/pi)