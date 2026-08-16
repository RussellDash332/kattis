from bisect import*;from itertools import*;N,*A=map(int,open(Z:=0));K=(0,1,2);P=[[0]for i in K]
for i in range(N):
 for j in K:P[j]+=[P[j][-1]+(A[i]==j)]
for a,b,c in permutations(K):
 S=[~N]
 for j in range(N+1):S+=[max(S[-1],P[b][~j]-P[c][~j])]
 for i in range(N+1):Z=max(Z,P[a][i]-P[b][i]+P[c][N]+S[~i])
print(Z)