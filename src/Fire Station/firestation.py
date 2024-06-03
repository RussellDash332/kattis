import sys; input = sys.stdin.readline; from heapq import *; from array import *
t = int(input()); input()
for _ in range(t):
    f, n = map(int, input().split()); INF = 10**9; ff = {int(input()) for _ in range(f)}; g = [{} for _ in range(n)]; best = (10**9, -1)
    while (s:=input().strip()): a, b, w = map(int, s.split()); g[a-1][b-1] = g[b-1][a-1] = w
    for i in range(n):
        D = array('i', [INF]*n); pq = [i]; ok = 1
        for j in ff: heappush(pq, j-1)
        for j in pq: D[j] = 0
        while pq:
            dv = heappop(pq); dd, vv = dv//n, dv%n
            if dd != D[vv]: continue
            for nn in g[vv]:
                if D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, new*n+nn)
        best = min(best, (max(D), i+1))
    print(best[1])