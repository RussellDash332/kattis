I=lambda:[*map(int,input().split())];N,M,B=I();P,R,S=zip(*(I()for _ in'.'*N));C=[[0]+I()for _ in'.'*N];D=[[0]+I()for _ in'.'*N];Z=[[1e9]*-~B for _ in'.'*-~N];Z[0][0]=0
for n in range(1,N+1):
 for b in range(B+1):Z[n][b]=min(max((R[n-1]+b-c-S[n-1]+D[n-1][m])*P[n-1],0)-C[n-1][m]+Z[n-1][c]for c in range(B+1)for m in range(M+1))
print(Z[N][0])