def mul(a, b):
    c = [[0]*len(b[0]) for _ in range(len(a))]
    for i, ci in enumerate(c):
        for j, ax in enumerate(a[i]):
            for k, by in enumerate(b[j]): ci[k] = (ci[k]+ax*by)%M
    return c
def matpow(m, k):
    if k == 0: return [[int(i==j) for j in range(len(m))] for i in range(len(m))]
    if k%2: return mul(matpow(m, k-1), m)
    return matpow(mul(m, m), k//2)
M = 10**9+7; N, P = map(int, input().split()); G = [[0]*N for _ in range(N)]
for _ in range(P): a, b = map(int, input().split()); G[a][b] += 1; G[b][a] += 1
print(matpow(G, int(input()))[0][0])