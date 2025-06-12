def mul(a, b):
    c = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N): c[i][j] += a[i][k]*b[k][j]; c[i][j] %= M
    return c

def matpow(m, k):
    if k == 0: return [[int(i==j) for j in range(N)] for i in range(N)]
    if k%2: return mul(matpow(m, k-1), m)
    s = mul(m, m); return matpow(s, k//2)

N, L = map(int, input().split()); M = 10**9+7; X = 19*pow(20, -1, M)%M; A = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    s = sum(A[i])
    if not s: A[i][i] = 1; continue
    for j in range(N): A[i][j] = A[i][j]*pow(s, -1, M)%M

Q = matpow(A, L)
for t in range(L, L+10): 
    if Q[0][-1] == X: print(t); exit()
    Q = mul(Q, A)
print(-1)