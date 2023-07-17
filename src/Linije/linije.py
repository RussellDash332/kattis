import sys; input = sys.stdin.readline
from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

V = 1000
g = [[] for _ in range(V)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    g[x-1].append(y+499), g[y+499].append(x-1)

match, mcbm = [-1]*V, 0
free = set(range(1000))
nfree = len(free)
for l in list(free):
    candidates = [r for r in g[l] if match[r] == -1]
    if candidates:
        mcbm += 1
        free.discard(l)
        match[choice(candidates)] = l
for f in free:
    vis = [0]*nfree
    mcbm += aug(f)
print(['Mirko', 'Slavko'][mcbm==sum(g[i]!=[] for i in range(1000))])