import sys; input = sys.stdin.readline
from math import *
r, s, m, d, n = map(int, input().split())
B = [*map(int, input().split())]
G = [set() for _ in range(s+m+d)]
S, M, D = [], [], []
for _ in range(s): S.append({*[*map(lambda x: int(x)-1, input().split())][1:]})
for _ in range(m): M.append({*[*map(lambda x: int(x)-1, input().split())][1:]})
for _ in range(d): D.append({*[*map(lambda x: int(x)-1, input().split())][1:]})
for _ in range(n): a, b = map(int, input().split()); G[a-1].add(b-1), G[b-1].add(a-1)
ans = 0
for i in range(s):
    for j in range(m):
        for k in range(d):
            if i not in G[s+j] and i not in G[s+m+k] and s+j not in G[s+m+k]:
                ans += prod(B[x] for x in S[i]|M[j]|D[k])
print(ans if ans <= 10**18 else 'too many')