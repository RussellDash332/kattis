import sys; input = sys.stdin.readline; from bisect import *
C, T = map(int, input().split())
A = [*map(lambda x: int(x)-1, input().split())]
B = [*map(lambda x: int(x)-1, input().split())]
P = [[] for _ in range(C)]
for i, x in enumerate(B): P[x] += [i]
Z = []
for i in range(C): P[i] = P[i][::-1]
for v in A:
    for p in P[v]:
        idx = bisect_left(Z, p)
        if idx == len(Z): Z.append(p)
        else: Z[idx] = p
print(len(Z))