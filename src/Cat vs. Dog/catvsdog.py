from random import choice
import sys; input = sys.stdin.readline

def solve():
    def aug(l):
        if vis[l]: return 0
        vis[l] = 1
        for r in g[l]:
            if match[r] == -1 or aug(match[r]): match[r] = l; return 1
        return 0
    C, D, v = map(int, input().split())
    V = 2*v
    g = [[] for _ in range(V)]
    match, mcbm = [-1]*V, 0
    free = set(range(v))
    nfree = len(free)
    votes = [input().strip().split() for _ in range(v)]
    for i in range(v-1):
        for j in range(i+1, v):
            if votes[i][0] == votes[j][1] or votes[i][1] == votes[j][0]: g[i].append(j+v), g[j].append(i+v)
    for l in list(free):
        candidates = [r for r in g[l] if match[r] == -1]
        if candidates:
            mcbm += 1
            free.discard(l)
            match[choice(candidates)] = l
    for f in free:
        vis = [0]*nfree
        mcbm += aug(f)
    print(v-mcbm//2)

for _ in range(int(input())): solve()