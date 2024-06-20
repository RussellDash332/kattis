import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from heapq import *; from array import *; K = 2000
n, m, p = map(int, input().split()); N = [complex(*map(int, input().split())) for _ in range(n)]; M = [complex(*map(int, input().split())) for _ in range(m)]; P = [complex(*map(int, input().split())) for _ in range(p)]; S = [(abs(N[i]-M[j]), K*i+j+n) for j in range(m) for i in range(n)]; T = [(abs(N[i]-P[j]), K*i+j+n) for j in range(p) for i in range(n)]; heapify(S); heapify(T); U1 = array('b', [0]*(n+m)); U2 = array('b', [0]*(n+p)); Z = X = 0
while X < n:
    d, ij = heappop(S)
    if not U1[ij//K] and not U1[ij%K]: Z += d; U1[ij//K] = U1[ij%K] = 1; X += 1
while X:
    d, ij = heappop(T)
    if not U2[ij//K] and not U2[ij%K]: Z += d; U2[ij//K] = U2[ij%K] = 1; X -= 1
print(Z)