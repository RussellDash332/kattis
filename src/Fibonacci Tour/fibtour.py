import sys
from collections import deque
v, e = map(int, input().split())
arr = list(map(int, input().split()))

fib = [1, 2]
while fib[-1] < 10**18: fib.append(fib[-1]+fib[-2])
fib = {e:i for i,e in enumerate(fib)}

hv = v
v *= 2
g, ind = [[] for _ in range(v)], [0]*v
for l in sys.stdin:
    a, b = map(int, l.split())
    a -= 1; b -= 1
    try:
        fa, fb = fib[arr[a]], fib[arr[b]]
        if fa == fb - 1:    g[a+hv].append(b+hv); ind[b+hv] += 1
        elif fa == fb + 1:  g[b+hv].append(a+hv); ind[a+hv] += 1
        if fa == fb == 0:
            g[a].append(b+hv); ind[b+hv] += 1
            g[b].append(a+hv); ind[a+hv] += 1
    except: pass
q, q2 = deque([i for i in range(v) if ind[i] == 0]), []
g.append(list(q))
while q:
    u = q.popleft()
    q2.append(u)
    for w in g[u]:
        ind[w] -= 1
        if ind[w] == 0: q.append(w)
d, p = [1e9]*(v+1), [-1]*(v+1)
d[v] = 0
for u in [v] + q2:
    for i in g[u]:
        if d[i] > d[u]-1: d[i], p[i] = d[u]-1, u
m = min(d)
bot, pt = [i for i in range(v) if d[i] == m and arr[i%hv] in fib], -1
if not bot: print(0)
else:
    bot = bot[0]
    while bot != -1: pt += 1; bot = p[bot]
    print(pt)