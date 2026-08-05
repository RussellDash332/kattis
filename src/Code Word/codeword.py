R,C,l=map(int,open(0).read().split());M=10**9+7;Z=[1]*R*C
for _ in'.'*~-l:
 S=sum(Z)%M;Y=[S]*R*C
 for i in range(R):
  for j in range(C):
   u=i*C+j
   for p in(-1,0,1):
    for q in(-1,0,1):
     if R>i+p>-1<j+q<C:Y[u]=(Y[u]-Z[u+p*C+q])%M
 Z=Y
print(sum(Z)%M)