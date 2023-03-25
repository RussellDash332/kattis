import sys
from math import gcd
input()
tog = 1
for line in sys.stdin:
    if tog: n = int(line)
    else:
        a, r, g, best = list(map(int, line.split())), {}, {}, 0
        for j in range(n):
            d = a[j]
            if d not in g: g[d] = j
            g2 = {}
            for i in g:
                k = gcd(i, d)
                if k not in g2: g2[k] = g[i]
                else: g2[k] = min(g2[k], g[i])
            g = g2
            best = max(best, max(k*(j+1-v) for k,v in g.items()))
        print(best)
    tog = 1-tog