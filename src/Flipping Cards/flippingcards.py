import sys
from collections import deque
T = V = -1
for l in sys.stdin:
    if T == -1: T = 1
    elif V == -1:
        V = v = int(l); g = [[] for _ in range(2*V)]
    elif v:
        a, b = map(int, l.split())
        a -= 1; b -= 1; v -= 1; g[a].append(b), g[b].append(a)
        if v == 0:
            vis, p = [0]*2*V, 0
            for i in range(2*V):
                if vis[i]: continue
                e = c = 0; q = deque([i])
                while q:
                    u = q.popleft()
                    if not vis[u]:
                        vis[u] = 1; c += 1; e += len(g[u])
                        for w in g[u]:
                            if not vis[w]: q.append(w)
                if 2*c < e: p = 1; break
            print('im'*p+'possible')
            V = -1