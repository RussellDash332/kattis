Z=101;D=[0]*Z*Z;D[1]=1
for n in range(1,Z):
 for k in range(1,n+1):D[n*Z+k]=D[n*Z-Z+k]*k+D[n*Z-Z+k-1]*(2*n-k)
for _ in'.'*int(input()):n,k=map(int,input().split());print(D[n*Z+k])