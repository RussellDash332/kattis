from heapq import *
import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
INF = 10**9
for _ in range(int(input())):
    n, m, s = map(int, input().split()); g = [{} for _ in range(n)]; T = int(input()); S = []; C = []
    for _ in range(m): a, b, f = map(int, input().split()); g[a-1][b-1] = g[b-1][a-1] = f
    for _ in range(s): v, c = map(int, input().split()); S.append(v-1); C.append(c)
    src, dst = map(int, input().split()); src -= 1; dst -= 1; G = []
    if dst not in S: S.append(dst); C.append(0)
    for ss in S:
        D = [INF]*n; D[ss] = 0; pq = [(0, ss)]; G.append([])
        while pq:
            dd, vv = heappop(pq)
            if dd != D[vv]: continue
            for nn in g[vv]:
                if D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, (new, nn))
        for t in S: G[-1].append(D[t])
    src = S.index(src); dst = S.index(dst)
    D = {}; D[src*INF] = 0; pq = [(0, src*INF)]
    while pq:
        dd, vc = heappop(pq); vv, cc = divmod(vc, INF)
        if vv == dst: print(dd); break
        if vc in D and dd != D[vc]: continue
        for nn in range(len(S)):
            ww = G[vv][nn]
            if ww > T: continue # tank cannot handle
            if cc <= ww: # fill sufficiently
                w = dd+(ww-cc)*C[vv]; k = nn*INF
                if k not in D or D[k] > w: D[k] = w; heappush(pq, (w, k))
            w = dd+(T-cc)*C[vv]; k = nn*INF+T-ww # full it
            if k not in D or D[k] > w: D[k] = w; heappush(pq, (w, k))