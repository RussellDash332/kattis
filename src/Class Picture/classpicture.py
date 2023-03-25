from collections import deque
from sys import stdin

n, m = 0, 0
for l in stdin:
    if n == m == 0:
        n, m, h = int(l), -1, {}
        g = {1<<i: {1<<i for i in range(n)} for i in range(n)}
    elif n > 0:
        n -= 1
        h[l.strip()] = 1<<len(h)
    elif n == 0:
        n, m = -1, int(l)
    else:
        m -= 1
        a, b = l.strip().split()
        r = {v: k for k, v in h.items()}
        g[h[a]].discard(h[b])
        g[h[b]].discard(h[a])
        if m == 0:
            path = None
            n, m = 0, 0
            t = (1<<len(h)) - 1
            q = deque(sorted([(1025*i, (i,)) for i in g], key=lambda x: r[x[0]//1025]))
            for i in g:
                g[i].discard(g[i])
                g[i] = sorted(g[i], key=lambda x: r[x])
            vis = set()
            while q:
                ub, p = q.popleft()
                if ub in vis: continue
                vis.add(ub)
                u, b = ub//1024, ub%1024
                if b == t: path = [r[i] for i in p]; break
                for v in g[u]:
                    if not (b&v): q.append((1024*v+(b+v), p+(v,)))
            if path == None: print('You all need therapy.')
            else: print(*path)