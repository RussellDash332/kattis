n,k=map(int,input().split());M=10**9+7
if n%k:print(0);exit()
F=[f:=1]+[f:=f*-~i%M for i in range(n)];print(F[n]*pow(pow(F[k],n//k,M)*F[n//k],-1,M)%M)