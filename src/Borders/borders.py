import sys; input = sys.stdin.readline
from random import choice
from collections import deque

R, C = map(int, input().split())
img = [input().strip() for _ in range(R)]
ime = [{i, i+C, (R+1)*C+(C+1)*(i//C)+(i%C), (R+1)*C+(C+1)*(i//C)+(i%C)+1} for i in range(R*C)]
el, elm = set(), {}
rep = [-1]*R*C
delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
q = deque()
for i in range(R*C):
    if not rep[i]+1:
        q.append(i)
        elm[i] = set()
        while q:
            u = q.popleft()
            if rep[u]+1: continue
            rep[u] = i
            elm[i] |= ime[u]
            rr, cc = u//C, u%C
            for dr, dc in delta:
                if 0<=rr+dr<R and 0<=cc+dc<C and img[rr][cc] == img[rr+dr][cc+dc]: q.append(u+dr*C+dc)
rev = {}
for i in elm:
    for j in elm[i]:
        if j not in rev: rev[j] = []
        rev[j].append(i)

base = set()
for i in range(C): base.add(rep[i]), base.add(rep[R*C-i-1])
for i in range(R): base.add(rep[i*C]), base.add(rep[(i+1)*C-1])
for i in rev:
    if rev[i][0] in base or rev[i][-1] in base: continue
    if len(rev[i]) == 1: continue
    el.add((rev[i][0], rev[i][-1])), el.add((rev[i][-1], rev[i][0]))

V = R*C
g = [[] for _ in range(V)]
for a, b in el: g[a].append(b)
match = [-1]*V
free = set(range(V))

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

mcbm = 0
for l in range(V):
    if (can:=[r for r in g[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(can)] = l
for f in free: vis = [0]*V; mcbm += aug(f)
print(mcbm//2 + len(base))