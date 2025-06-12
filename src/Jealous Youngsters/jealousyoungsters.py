from collections import *
n, m = map(int, input().split())
d, e = map(int, input().split())
h = [[] for _ in range(n)]
for _ in range(e): s, k, t = map(int, input().split()); k -= 1; t -= 1; h[k].append((s, t))
u = [[] for _ in range(n)]
for i in range(n):
    p = -1; c = 0
    for s, t in h[i]:
        if t != p:
            if p != -1: u[i].append((p, s-c))
            p, c = t, s
    if p != -1: u[i].append((p, d-c))
v = [[0]*n for _ in range(m)]
z = [[] for _ in range(n)]
for i in range(n):
    ss = set()
    for t, q in u[i]: v[t][i] += q; t in ss or z[i].append(t); ss.add(t)
    z[i].extend({*range(m)}-ss)
l = [*map(deque, z)]; pr = {}; A = {*range(n)}
while A:
    aa = A.pop()
    if not l[aa]: print('impossible'); exit()
    bb = l[aa].popleft()
    if bb not in pr: pr[bb] = aa
    elif v[bb][a0:=pr[bb]] < v[bb][aa]: A.add(aa)
    else: A.add(a0); pr[bb] = aa
Z = [-1]*n
for b, a in pr.items(): Z[a] = b+1
print(*Z)