import sys; sys.setrecursionlimit(5000)
N = int(input())
rev, el, m = {}, [], []
for l in sys.stdin:
    a, b = l.strip().split()
    if a not in rev: rev[a] = len(rev); m.append(a)
    if b not in rev: rev[b] = len(rev); m.append(b)
    el.append((rev[a], rev[b]))
V = len(rev)
g, gt = [[] for _ in range(V)], [[] for _ in range(V)]
for a, b in el: g[a].append(b), gt[b].append(a)
top, vis, scc = [], set(), []
def DFS(s, add):
    vis.add(s)
    a = gt if add else g
    for v in a[s]:
        if v not in vis: DFS(v, add)
    if add: top.append(s)
    else: scc[-1].append(m[s])
for i in range(V):
    if i not in vis: DFS(i, True)
vis.clear()
for i in top[::-1]:
    if i not in vis: scc.append([]), DFS(i, False)
for i in scc: i.sort()
scc.sort(key=lambda x: (len(x)<2, x))
avoid = []
for i in scc:
    if len(i) > 1: print('okay', ' '.join(i))
    else: avoid.append(i[0])
if avoid: print('avoid', ' '.join(sorted(avoid)))