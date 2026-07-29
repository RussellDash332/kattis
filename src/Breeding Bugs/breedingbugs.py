from random import *
def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

from array import *
LIMIT = 2*10**7+67
F = array('I', [0]*LIMIT)
P = array('I')
for i in range(2, LIMIT):
    if F[i] < 1: F[i] = i; P.append(i)
    for p in P:
        if (j:=i*p) >= LIMIT: break
        F[j] = p
        if p == F[i]: break

V, *p = map(int, open(0).read().split())
p.sort(reverse=1)
while len(p)>1 and p[-2]==p[-1]==1: p.pop(); V -= 1
p.sort(key=lambda x:1-x%2)
g = [[] for _ in range(V)]
for i in range(V):
    for j in range(i):
        if F[u:=p[i]+p[j]] == u: g[i] += [j]; g[j] += [i]
match, mcbm = [-1]*V, 0
free = {i for i in range(V) if p[i]%2}; nfree = len(free)
for l in [*free]:
    if (candidates:=[r for r in g[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
for f in free: vis = [0]*nfree; mcbm += aug(f)
print(V-mcbm)