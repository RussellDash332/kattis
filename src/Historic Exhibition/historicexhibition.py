from collections import *
p, v = map(int, input().split()); P = [[] for _ in range(10067)]; Q = [[] for _ in range(10067)]; Z = [0]*v
for i in range(p):
    a, b = map(int, input().split())
    if a > b: a, b = b, a
    (Q, P)[b-a][a] += [i+1]
V = [[] for _ in range(10067)]
for i, e in enumerate(map(int, input().split())): V[e] += [i]
for i in range(10067):
    while Q[i] and V[i]: Z[V[i].pop()] = Q[i].pop()
for i in range(1, 10067):
    while P[i-1] and V[i]: Z[V[i].pop()] = P[i-1].pop()
    while P[i] and V[i]: Z[V[i].pop()] = P[i].pop()
if min(Z, default=1): print(*Z)
else: print('impossible')