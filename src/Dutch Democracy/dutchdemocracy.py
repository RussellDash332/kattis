N, *A = map(int, open(0).read().split()); A.sort(); U = sum(A); Z = 0; D = [[1]+[0]*U]
for i in range(N-1):
    D.append([*D[-1]])
    for j in range(U-A[~i], -1, -1): D[-1][j+A[~i]] += D[-2][j]
for i in range(N):
    s = A[i]; K = D.pop()
    for t in range(U//2-s+1, U//2+1): Z += K[t]
print(Z)