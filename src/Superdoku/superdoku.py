from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

n, k = map(int, input().split())
g = [[] for _ in range(2*n)]
possible = [set(range(n)) for _ in range(n)]
sdk = [['yes']]
for _ in range(k):
    row = list(map(int, input().split()))
    sdk.append(row)
    for i in range(n): possible[i].discard(row[i]-1)
for i in range(n):
    g[i] = list(map(lambda x: x+n, possible[i]))
    if len(g[i]) != n-k: print('no'); exit(0)

try:
    for _ in range(n-k):
        match, mcbm = [-1]*(2*n), 0
        free = set(range(n))
        for l in range(n):
            candidates = [r for r in g[l] if match[r] == -1]
            if candidates:
                mcbm += 1
                free.discard(l)
                match[choice(candidates)] = l
        for f in free:
            vis = [0]*n
            mcbm += aug(f)
        row = [-1]*n
        for i in range(n): row[match[i+n]] = i+1; g[match[i+n]].remove(i+n)
        sdk.append(row)
    for row in sdk: print(*row)
except: print('no')