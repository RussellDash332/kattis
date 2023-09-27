import sys; input = sys.stdin.readline
from collections import *

def lis(arr):
    def upper_bound(sub, idx):
        lo, hi = 0, len(sub) - 1
        while hi > lo:
            mid = (lo + hi) // 2
            if arr[sub[mid]] < arr[idx]: lo = mid + 1
            else: hi = mid
        return hi
    temp = []; par = [None]*len(arr)
    for i in range(len(arr)):
        if not temp or arr[i] > arr[temp[-1]]:
            if temp: par[i] = temp[-1]
            temp.append(i)
        else:
            rep = upper_bound(temp, i); temp[rep] = i
            if rep != 0: par[i] = temp[rep - 1]
    final = 0; curr = temp[-1]
    while curr != None: final += 1; curr = par[curr]
    return final

n, m, d = map(int, input().split()); g = {}; indeg = Counter(); top = []
for _ in range(m):
    a, b = map(int, input().split())
    if a not in g: g[a] = set()
    if b not in g[a]: g[a].add(b); indeg[b] += 1; indeg[a] = indeg[a]
q = deque([i for i in indeg if indeg[i] == 0])
while q:
    u = q.popleft()
    top.append(u)
    if u not in g: continue
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)
aa = [int(input()) for _ in range(n)]
c = []; r = {e:i for i,e in enumerate(top)}
for i in range(len(aa)):
    if aa[i] in r: c.append(r[aa[i]])
print(len(top)+n-2*(lis(c) if c else 0))