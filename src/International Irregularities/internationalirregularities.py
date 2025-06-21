import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, q, m = map(int, input().split()); r = [*map(int, input().split())]; t = [*map(int, input().split())]; J = [[None]*18 for _ in range(n)]; p = 0; S = [t[0]]; b = n-1; T = [t[-1]+1]
for i in range(n):
    while p+1 < n and r[p+1]-r[i] <= m: p += 1
    J[i][0] = p
for i in range(1, n): S.append(min(t[i], S[-1]))
for i in range(1, 18):
    for j in range(n): J[j][i] = J[J[j][i-1]][i-1]
def f(x, y):
    if x > y: return f(y, x)
    if J[x][17] < y: return 10**18
    z = 1
    for i in range(17, -1, -1):
        if J[x][i] < y: z += 1<<i; x = J[x][i]
    return z
for i in range(n-2, -1, -1):
    if (u:=f(i, b)) == 10**18 or t[i]+1 < (v:=u+T[n-1-b]): T.append(t[i]+1); b = i
    else: T.append(v)
for _ in range(q): x, y = map(int, input().split()); x -= 1; y -= 1; print(1 if r[x] < r[y] else min(f(x, y), t[y]+1, S[y]+2, T[~y]))