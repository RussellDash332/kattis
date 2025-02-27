import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from math import *; from array import *; from collections import *
v, e, k = map(int, input().split())
w = array('i', (int(i)-1 for i in input().split()))
g = [[] for _ in range(v)]
for _ in range(e): a, b = map(int, input().split()); g[a-1].append(b-1); g[b-1].append(a-1)
d = array('i', [v+1]*v); e = array('i', [v+1]*v); d[0] = e[-1] = 0
q = deque([0])
while q:
    u = q.popleft()
    for x in g[u]:
        if d[x] == v+1: d[x] = d[u]+1; q.append(x)
q = deque([v-1])
while q:
    u = q.popleft()
    for x in g[u]:
        if e[x] == v+1: e[x] = e[u]+1; q.append(x)
s = sum(e[i] for i in w); z = d[-1]*(k-1)
for i in w: z = min(z, d[i]*(k-1)+s-e[i])
g = gcd(z, k-1); print(f'{z//g}/{(k-1)//g}')