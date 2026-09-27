from bisect import*;N,*A=map(int,open(0).read().split());A.sort();D=[0]*-~N
for i in range(N)[::-1]:
 for j in range(2,5):D[i]=max(D[i],D[bisect_left(A,A[i]+j*1e5)]+j)
print(D[0])