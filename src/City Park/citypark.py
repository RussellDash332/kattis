import sys; input = sys.stdin.readline
from collections import *
class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N; s.a = [0]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x; s.a[x] += s.a[y]
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]; s.a[y] += s.a[x]
N = int(input()); U = UFDS(N); RXO, RXC, RYO, RYC = [defaultdict(list) for _ in range(4)]
for i in range(N):
    X, Y, W, H = map(int, input().split()); U.a[i] = W*H
    RXO[X].append((Y, Y+H, i)), RXC[X+W].append((Y, Y+H, i))
    RYO[Y].append((X, X+W, i)), RYC[Y+H].append((X, X+W, i))
def merge(arr):
    ptr = 0
    for i in range(1, len(arr)):
        if arr[ptr][1] >= arr[i][0]: U.union(arr[ptr][2], arr[i][2]); arr[ptr][1] = max(arr[ptr][1], arr[i][1])
        else: ptr += 1; arr[ptr] = arr[i]
for x in RXO:
    if x in RXC: merge(sorted(map(list, RXO[x] + RXC[x])))
for y in RYO:
    if y in RYC: merge(sorted(map(list, RYO[y] + RYC[y])))
print(max(U.a[i] for i in range(N) if U.p[i] == i))