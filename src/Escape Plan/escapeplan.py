import sys; input = sys.stdin.readline
from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

s = 1
while True:
    m = int(input())
    if m == 0: break
    robots = [complex(*map(float, input().split())) for _ in range(m)]
    n = int(input())
    holes = [complex(*map(float, input().split())) for _ in range(n)]
    V = m+n
    g = [set() for _ in range(V)]
    print('Scenario', s)
    for k in [50, 100, 200]:
        for i in range(m):
            for j in range(n):
                if abs(robots[i]-holes[j]) <= k: g[i].add(j+m)
        match, mcbm = [-1]*V, 0
        free = set(range(m))
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
        print(f'In {k//10} seconds {mcbm} robot(s) can escape')
    s += 1; print()