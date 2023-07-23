import sys; input = sys.stdin.readline
from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

for _ in range(int(input())):
    F = []; N = int(input()); V = 2*N
    g = [[] for _ in range(V)]
    for _ in range(N):
        t, *p = input().split()
        a, b, c, d = map(int, p)
        h, m = t.split(':'); t = 60*int(h)+int(m)
        F.append((a, b, c, d, t))
    for i in range(N):
        a, b, c, d, t = F[i]
        for j in range(N):
            if i == j: continue
            a2, b2, *_, t2 = F[j]
            if (t+abs(a-c)+abs(b-d)+abs(c-a2)+abs(d-b2)+1)%14400 <= t2: g[i].append(j+N)
    match, mcbm = [-1]*V, 0
    free = set(range(N))
    nfree = N
    for l in list(free):
        candidates = [r for r in g[l] if match[r] == -1]
        if candidates:
            mcbm += 1
            free.discard(l)
            match[choice(candidates)] = l
    for f in free:
        vis = [0]*nfree
        mcbm += aug(f)
    print(N-mcbm)