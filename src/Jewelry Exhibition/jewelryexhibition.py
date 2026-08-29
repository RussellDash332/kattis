from random import *
def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in G[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0
for _ in range(int(input())):
    R, C, N = map(int, input().split()); V = R+C; G = [[] for _ in range(V)]
    for _ in range(N):
        x, y = map(float, input().split()); x = int(x); y = int(y)
        G[x] += [y+R]; G[y+R] += [x]
    match, mcbm = [-1]*V, 0; free = {*range(R)}
    for l in [*free]:
        if (candidates:=[r for r in G[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
    for f in free: vis = [0]*R; mcbm += aug(f)
    print(mcbm)