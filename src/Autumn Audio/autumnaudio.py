from collections import *
N, *T = map(int, open(0).read().split()); Z = set()
for i in range(1, N):
    d = T[i]-T[0]
    if d<1 or d in Z: continue
    c = Counter(T)
    for i in T:
        if c[i] and c[i+d]: c[i] -= 1; c[i+d] -= 1
    if sum(c.values())<1: Z.add(d)
print(len(Z), *sorted(Z))