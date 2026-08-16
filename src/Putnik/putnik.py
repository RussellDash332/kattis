N=int(input());G=[[*map(int,input().split())]for _ in'.'*N];D=[[10**9]*N for _ in'.'*N];D[0][0]=0
for i in range(1,N):
 for j in range(i):D[i][j]=min(D[i][j],D[i-1][j]+G[i-1][i]);D[i][i-1]=min(D[i][i-1],D[i-1][j]+G[j][i])
print(min(D[-1]))