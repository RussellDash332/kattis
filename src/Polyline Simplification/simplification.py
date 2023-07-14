import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from heapq import *

class Node:
    def __init__(self, v):
        self.p, self.n, self.v = None, None, v
    def remove(self):
        if self.p: self.p.n = self.n
        if self.n: self.n.p = self.p

ans = []
n, m = map(int, input().split())
pts = [[*map(int, input().split())] for _ in range(n+1)]
nm, pq, used = {}, [], [0]*(n+1)
for i in range(n+1):
    nm[i] = Node(i)
    if i-1 in nm: nm[i-1].n, nm[i].p = nm[i], nm[i-1]
    if i+1 in nm: nm[i+1].p, nm[i].n = nm[i], nm[i+1]
for i in range(n-1): (x1, y1), (x2, y2), (x3, y3) = pts[i], pts[i+1], pts[i+2]; pq.append((abs(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2), i+1, i, i+2))
heapify(pq); k = n-m
while True:
    _, c, a, b = heappop(pq)
    if used[a] or used[b] or used[c]: continue
    p = nm[c].p; pp = p.p; s = nm[c].n; ss = s.n; nm[c].remove(), ans.append(c); used[c] = 1
    if len(ans) == k: break
    if pp: (x1, y1), (x2, y2), (x3, y3) = pts[pp.v], pts[p.v], pts[s.v]; heappush(pq, (abs(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2), p.v, pp.v, s.v))
    if ss: (x1, y1), (x2, y2), (x3, y3) = pts[p.v], pts[s.v], pts[ss.v]; heappush(pq, (abs(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2), s.v, p.v, ss.v))
sys.stdout.write('\n'.join(map(str, ans)))