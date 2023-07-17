import sys; input = sys.stdin.readline
V, E = map(int, input().split())
animals = []
currs = []
for _ in range(V):
    ani, _, *curr = input().strip().split()
    animals.append(ani), currs.append(curr)
rev = {e:i for i,e in enumerate(animals)}
g = [[] for _ in range(V)]
di, do = [0]*V, [0]*V
for i in range(V):
    for j in currs[i]:
        if animals[i] != j: do[i] += 1; di[rev[j]] += 1; g[i].append(rev[j]), g[rev[j]].append(i)
if sum(di) == sum(do) == 0: print('FALSE ALARM'), exit(0)
for i in range(V):
    if g[i]:
        stack, vis = [i], set()
        while stack:
            u = stack.pop()
            if u in vis: continue
            vis.add(u)
            for v in g[u]: stack.append(v)
        break
cc = 0
for i in range(V):
    if g[i]: cc += 1
p1, m1, same = [], [], []
l = [same, p1, m1]
for i in range(V):
    if -1<=di[i]-do[i]<=1: l[di[i]-do[i]].append(i)
print(['IMPOSSIBLE', 'POSSIBLE'][len(vis) == cc and (len(p1), len(m1), len(same)) in [(0, 0, V), (1, 1, V-2), (1, 0, V-1), (0, 1, V-1)]])