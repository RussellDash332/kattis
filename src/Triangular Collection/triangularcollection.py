N,*A=map(int,open(Z:=0));A.sort()
for i in range(N):
 for j in range(i+1,N):Z+=2**sum(A[i]+A[j]>A[k]for k in range(j+1,N))-1
print(Z)