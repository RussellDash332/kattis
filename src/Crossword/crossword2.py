n = int(input()); M = [input() for _ in range(n)]; R = {}; S = {}; s = -1
for i in range(n):
    j = 0
    while j < n:
        if M[i][j] != 'X':
            s += 1
            while j < n and M[i][j] != 'X':
                if M[i][j] == '-': R[(i, j)] = s
                j += 1
        j += 1
    j = 0
    while j < n:
        if M[j][i] != 'X':
            s += 1
            while j < n and M[j][i] != 'X':
                if M[j][i] == '-': S[(j, i)] = s
                j += 1
        j += 1

from random import *
def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0
V = s+1; g = [[] for _ in range(V)]
for p in R: g[R[p]] += [S[p]]
match, mcbm = [-1]*V, 0
free = {*range(V)}
for l in [*free]:
    if (candidates:=[r for r in g[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
for f in free: vis = [0]*V; mcbm += aug(f)
print(mcbm)