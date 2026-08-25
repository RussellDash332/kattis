N,K,*A=map(int,open(0).read().split());S=[0];H=[0]*-~N;E=[*enumerate(A)];F=[1]+[0]*N
for i,e in E:H[e]=i
for i,e in E:
 if 1-F[e]:
  while i<H[S[-1]]and S[-1]>e:F[S.pop()]=0
  S+=[e];F[e]=1
print(*S[1:])