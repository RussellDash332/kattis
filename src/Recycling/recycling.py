N,*A=map(int,open(0).read().split());S=[-1];A+=[0];Z=(0,0,0)
for i in range(N+1):
 while S and A[i]<A[S[-1]]:Z=max(Z,(A[S.pop()]*(i-S[-1]-1),-S[-1]-2,i))
 S+=[i]
z,s,e=Z
if z:print(-s,e,z)
else:print(1,1,0)