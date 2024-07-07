N,*A=map(int,open(W:=0).read().split());V=[Z:=0]*N
for i in range(N):t=i<N/2;V[A[i]-1]=1-t;Z+=(2*t-1)*A[i]+i*t
for i in V:Z-=(W:=W+i)*(1-i)
print(Z)