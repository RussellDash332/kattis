import sys
from collections import deque

n, m = map(int, input().split())
p, rn = [], range(n)
for line in sys.stdin:
    p.extend(map(int, line.split()))
    if len(p) == n: break
g, ccs = tuple([] for _ in rn), set(rn)
for line in sys.stdin:
    a, b = map(int, line.split())
    a -= 1
    g[b-1].append(a)
    if a in ccs: ccs.remove(a)
pp, q, ans, get = [], deque(), 1e9, lambda x: p[x]
for cc in ccs:
    q.clear()
    q.append(cc)
    vis = {cc}
    while q:
        for u in g[q.popleft()]:
            if u not in vis:
                vis.add(u)
                q.append(u)
    for v2 in pp: ans = min(ans, sum(map(get, v2|vis)))
    pp.append(vis)
print(ans)