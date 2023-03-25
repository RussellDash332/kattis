import sys
from bisect import *
from heapq import *
m, m2, h, q = int(input()), 0, {}, -1
for line in sys.stdin:
    if m2 != m:
        m2 += 1
        p, v = map(int, line.split())
        if v not in h: h[v] = []
        h[v].append(200000*p - m2)
    elif q == -1:
        q, a = 0, {}
        vv = sorted(h)
        tmp = []
        for v2 in vv:
            for i in h[v2]:
                heappush(tmp, i)
                if len(tmp) > 10: heappop(tmp)
            a[v2] = sorted(tmp, reverse=True)
        tmp.clear()
    else:
        x, k = map(int, line.split())
        if x < vv[0]: print(-1)
        else:
            check = a[vv[bisect_right(vv, x)-1]]
            for i in range(min(k, len(check))): tmp.append(-check[i]%200000)
            if not tmp: print(-1)
            else: print(*tmp); tmp.clear()