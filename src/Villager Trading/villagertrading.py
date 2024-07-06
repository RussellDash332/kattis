import sys; input = sys.stdin.readline; from math import *
R = {'Emerald': 0, '@': 1}; E = []; INF = float('inf')
for _ in range(int(input())):
    for _ in range(int((input()))):
        p, a, q, b = input().strip().split()
        if a not in R: R[a] = len(R)
        if b not in R: R[b] = len(R)
        E.append((R[a], R[b], log(int(p))-log(int(q))))
D = [INF]*len(R); D[1] = 0
for i in range(2, len(R)): E.append((1, i, 0))
for _ in range(len(R)-1):
    for a, b, w in E: D[b] = min(D[b], D[a]+w)
Z = D[0]
for _ in range(len(R)-1): # could've checked more efficiently like /xyzzy but this works anyways'
    for a, b, w in E: D[b] = min(D[b], D[a]+w)
    if D[0] != Z: print('yes'), exit(0)
print('no')