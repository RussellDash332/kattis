import sys; input = sys.stdin.readline
from heapq import *
while True:
    n, m, a, k = map(int, input().split())
    if n==m==a==k==0: break
    g = [{} for _ in range(n)]
    for _ in range(m):
        t1, t2, w = map(int, input().split())
        t1 -= 1; t2 -= 1; g[t1][t2] = g[t2][t1] = w
    bs = [int(input())-1 for _ in range(a)]
    D = [1e9]*n
    pq = []
    safe = set(range(n))
    for i in bs:
        D[i] = 0
        heappush(pq, (0, i))
        while pq:
            dd, vv = heappop(pq)
            if dd < k: safe.discard(vv)
            else: break
            if dd == D[vv]:
                for nn in g[vv]:
                    if D[nn] > dd + g[vv][nn]:
                        D[nn] = dd + g[vv][nn]
                        heappush(pq, (D[nn], nn))
        print(len(safe))
    print()