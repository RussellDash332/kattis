import sys; input = sys.stdin.readline; from collections import *
N, M = map(int, input().split())
S = input(); T = input()
G = [[] for _ in range(N)]
for _ in range(M): a, b = map(int, input().split()); G[a-1].append(b-1); G[b-1].append(a-1)
V = [0]*N
for i in range(N):
    if V[i]: continue
    c = [i]; V[i] = 1; P = Counter(); Q = Counter()
    for u in c:
        for v in G[u]:
            if not V[v]: V[v] = 1; c.append(v)
    for u in c: P[S[u]] += 1; Q[T[u]] += 1
    if P != Q: print('No'); break
else: print('Yes')