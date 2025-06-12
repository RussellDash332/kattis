import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
v = int(input()); g = [[] for _ in range(v)]; s = [0]*v; z = []; c = 0
for i in range(v):
    k, *x = map(int, input().split())
    for j in x: g[j-1].append(i)
for x in [int(input())-1 for _ in range(v)][::-1]:
    t = [x]
    for u in t:
        if not s[u]: s[u] = 1; c += 1; t.extend(g[u])
    z.append(v-c)
print(*z[-2::-1]+[v])