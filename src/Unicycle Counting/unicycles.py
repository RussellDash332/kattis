import sys; input = sys.stdin.readline
while (s:=input().strip().split()):
    n, m, *k = map(int, s); c = []; k.sort(); h = {e:1<<i for i,e in enumerate(k)}; M = 1<<m; K = [10**9]*M; K[0] = 0
    for i in range(m):
        c.append(1<<i)
        for j in range(i+1, m):
            d = k[j]-k[i]; ok = 1
            if d <= k[i]: continue
            p = k[i]; b = 0
            while p < n:
                if p not in h: ok = 0; break
                b |= h[p]; p += d
            if ok: c.append(b)
    for i in c:
        for j in range(M-1, -1, -1):
            if j|i < M: K[j|i] = min(K[j|i], K[j]+1)
    print(K[-1])