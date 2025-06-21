N,*B=map(int,open(0).read().split());D=[0]*N*(N+1)
for j in range(1,N+1):
 for i in range(N-j+1):D[j*N+i]=0if j<2else B[i*N+i+1]if j<3else max(D[j*N+i-N],*(D[k*N+i]+B[(i+j-1)*N+i+k]+D[(j-k-2)*N+i+k+1]for k in range(j-1)))
print(D[-N])