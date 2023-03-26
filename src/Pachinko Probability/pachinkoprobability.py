import sys
from collections import deque

v, e, k = int(input()), int(input()), -1
g, x = [[] for _ in range(v)], []
for line in sys.stdin:
    if e > 0:
        e -= 1
        a, b = map(int, line.split())
        g[a].append(b)
    elif k == -1:
        e = -1
        k = int(line)
    else:
        k -= 1
        x.append(int(line))

top, indeg, q = [], [0]*v, deque([])
for u in range(v):
    for w in g[u]: indeg[w] += 1
for u in range(v):
    if indeg[u] == 0: q.append(u)
top, q2 = [], list(q)
while q:
    u = q.popleft()
    top.append(u)
    for w in g[u]:
        indeg[w] -= 1
        if indeg[w] == 0: q.append(w)

dp = [0]*v
for i in x: dp[i] = 1
for i in range(v):
    if dp[i] != 1 and not g[i]: dp[i] = 1j
for i in top[::-1]:
    for j in g[i]:
        dp[i] += dp[j]

r = 0
for i in q2: r += dp[i]
print(f'''winning paths {int(r.real)}
total paths {int(r.real+r.imag)}''')