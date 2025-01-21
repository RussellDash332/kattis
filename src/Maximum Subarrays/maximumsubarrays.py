N, K, *A = map(int, open(0).read().split()); Z = -10**18
B = [[0] for _ in range(N)]; I = [[Z] for _ in range(N)]
B[0] += [A[0]]+[Z]*K; I[0] += [A[0]]+[Z]*K
for i in range(1, N):
    for j in range(1, K+1): I[i].append(v:=max(I[i-1][j], B[i-1][j-1])+A[i]); B[i].append(max(B[i-1][j], v))
print(B[-1][-1])