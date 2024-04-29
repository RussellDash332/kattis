import sys; input = sys.stdin.readline
n, m = map(int, input().split()); n += 1; g = [{} for _ in range(n)]; dp = [0]*n; high = 0; I = [0]*n; v = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    if b not in g[a]: g[a][b] = 0
    g[a][b] += 1
q = [1]; dp[2] = 1; T = []
for u in q:
    if v[u]: continue
    v[u] = 1; q.extend(g[u])
for i in range(n):
    if v[i]:
        for j in g[i]:
            if v[j]: I[j] += 1
tq = [i for i in range(n) if I[i] == 0 and v[i]]
for u in tq:
    T.append(u)
    for x in g[u]:
        I[x] -= 1
        if I[x] == 0 and v[x]: tq.append(x)
if 2 not in T: print('inf'), exit(0)
while T:
    u = T.pop()
    for x in g[u]:
        dp[u] += g[u][x]*dp[x]
        if dp[u] >= 10**9: high = 1
    if high: dp[u] %= 10**9
print(dp[1] if not high else str(dp[1]).zfill(9))