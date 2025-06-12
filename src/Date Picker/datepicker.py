from itertools import *
M = [[int(s=='.') for s in input()] for _ in range(7)]
d, h = map(int, input().split()); z = 0
for p in combinations(range(7), d):
    v = [0]*24
    for i in p:
        for j in range(24): v[j] += M[i][j]
    z = max(z, sum(sorted(v)[-h:]))
print(z/d/h)