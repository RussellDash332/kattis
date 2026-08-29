import sys; input = sys.stdin.readline; from heapq import *
n = int(input()); G = [[] for _ in range(n)]; C = []
for i in range(n):
    m, t = map(int, input().split()); C += [t]
    for _ in range(m): s, x, *a = map(int, input().split()); G[i] += [(x-1, {*a})]
INF = 10**9; D = {}; D[(0, -1)] = C[0]; pq = [(C[0], 0, -1)]
while pq:
    dd, vv, p = heappop(pq)
    if (vv, p) in D and dd != D[(vv, p)]: continue
    for nn, aa in G[vv]:
        new = dd+C[nn]
        if p+1 not in aa and ((nn, vv) not in D or D[(nn, vv)] > new): D[(nn, vv)] = new; heappush(pq, (new, nn, vv))
print(min([D[i] for i in D if i[0]==n-1], default='impossible'))