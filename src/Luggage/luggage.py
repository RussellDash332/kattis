import sys; input = sys.stdin.readline; from math import *

def merge(intervals):
    r = []
    for j in intervals:
        if r and r[-1][1] >= j[0] and j[1] >= r[-1][0]: r[-1] = (min(r[-1][0], j[0]), max(r[-1][1], j[1]))
        else: r.append(j)
    return r

N, L = map(int, input().split()); X = [*map(float, input().split())]; K = []
if N == 1: print(10), exit(0)
for i in range(N):
    for j in range(i): K.append(abs(X[i]-X[j]))
T = [(min(K), float('inf'))]
for k in {*K}:
    for n in range(1, ceil((10*k+1)/L)):
        if (v:=k/(n*L+1)) > T[0][0]: continue
        T.append((v, k/(n*L-1)))
T.sort(); T = merge(T); U = [(0, T[0][0])]; V = []
for i in range(len(T)-1): U.append((T[i][1], T[i+1][0]))
for s, e in T:
    ns, ne = max(s, 0.1), min(e, 10)
    if ns <= ne: V.append((ns, ne))
if V[-1][0] <= 0.1: print('no fika'), exit(0)
print(V[-1][0])