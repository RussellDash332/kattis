import sys; input = sys.stdin.readline
V = int(input())
g = [[] for _ in range(V)]
ind = [0]*V
for i in range(V): g[i].append(int(input())-1); ind[g[i][-1]] += 1
free, mob, civ = set(range(V)), [], []
while True:
    while True:
        bef = len(mob)
        for i in [*free]:
            if ind[i] == 0:
                mob.append(i), free.discard(i)
                for j in g[i]:
                    if j in free:
                        civ.append(j), free.discard(j)
                        for k in g[j]:
                            if k in free: ind[k] -= 1
        if len(mob) == bef: break
    if not free: break
    for i in free:
        civ.append(i)
        for j in g[i]:
            if j in free: ind[j] -= 1
        break
    free.discard(i)
print(len(mob))