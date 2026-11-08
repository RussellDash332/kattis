import sys, os; from collections import *; print = sys.stdout.write
c = 0; W = []; F = W.append
for i in os.read(0, 3_670_067):
    if i > 45: c = c*10+i-48
    elif c: F(c); c = 0
N = W[0]
if N%2<1: print('IMPOSSIBLE'); exit()
G = [[] for _ in range(N)]
for a, b in zip(W[1::2], W[2::2]): G[a-1] += [b-1]; G[b-1] += [a-1]
I = [0]*N; D = [*map(len, G)]; Q = deque(i for i in range(N) if D[i]==1); B = []
for _ in range(N//2):
    a = Q.popleft(); b = Q.popleft(); p = G[a][I[a]]; q = G[b][I[b]]
    while D[p]<1: I[a] += 1; p = G[a][I[a]]
    while D[q]<1: I[b] += 1; q = G[b][I[b]]
    print(f'{p+1} {a+1}\n{a+1} {b+1}\n'); B += [(q, b), (a, b)]; D[a] = D[b] = 0; D[p] -= 1; D[q] -= 1
    if D[p]==1: Q += [p]
    if D[q]==1 and q!=p: Q += [q]
for a, b in B: print(f'{a+1} {b+1}\n')