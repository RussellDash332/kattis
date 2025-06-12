import sys; input = sys.stdin.readline; M = 10**9+7
def det(a):
    z = 1; n = len(a)
    for i in range(n):
        k = i
        for j in range(i+1, n):
            if a[j][i] > a[k][i]: k = j
        if a[k][i] == 0: z = 0; break
        a[i], a[k] = a[k], a[i]
        if i != k: z = -z
        z *= a[i][i]; z %= M
        for j in range(i+1, n): a[i][j] = a[i][j]*pow(a[i][i], -1, M)%M
        for j in range(n):
            if j != i and a[j][i]:
                for k in range(i+1, n): a[j][k] = (a[j][k]-a[i][k]*a[j][i])%M
    return z
n, m = map(int, input().split())
s, t = map(int, input().split()); s -= 1; t -= 1
L = [[0]*n for _ in range(n)]
for _ in range(m): a, b, r = map(int, input().split()); v = pow(r, -1, M); L[a-1][b-1] -= v; L[b-1][a-1] -= v
for i in range(n):
    L[i][i] = -sum(L[i])
    for j in range(n): L[i][j] %= M
print(det([[L[i][j] for j in range(n) if j not in (s, t)] for i in range(n) if i not in (s, t)])*pow(det([l[1:] for l in L[1:]]),-1,M)%M)