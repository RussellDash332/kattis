I=lambda:map(int,input().split());n,s=I();N=2167;D=[0]+[1e18]*N
for _ in'.'*n:
 k,l,x=I()
 for _ in'.'*k:
  for i in range(N-l)[::-1]:D[i+l]=min(D[i+l],D[i]+x)
Z=min(D[s:]);print(Z if Z<1e18else'impossible')