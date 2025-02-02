N,M=map(int,input().split());Z=[0]*N
for i in range(M):
 A=[*map(int,input().split())]
 for j in range(N//2):Z[A[j]-1]|=1<<i
print('YNEOS'[len({*Z})<N::2])