N,L,p=map(eval,input().split());P=[p**i for i in range(N+1)];P[1]=0;D=[[0]*L+[1]for _ in'.'*-~N];D[0][L]=0
for n in range(1,N+1):
 for l in range(L)[::-1]:D[n][l]=P[n]*D[n-1][l]+(1-P[n])*(D[n-1][l+1]+D[n][l+1])/2
print(D[N][0])