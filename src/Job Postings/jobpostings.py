INF = 10**18
def add(u, v, c, w): e1, e2 = [u, v, c, w, 0, len(al[v])], [v, u, 0, -w, 0, len(al[u])]; al[u].append(len(el)), el.append(e1), al[v].append(len(el)), el.append(e2)
while True:
    N, M = map(int, input().split()); P = [int(input()) for _ in range(N)]; n = N+M+2; s = n-2; t = n-1; al, el, k = [[] for _ in range(n)], [], INF; flow = cost = 0
    if N < 1: break
    for i in range(N): add(s, i, P[i], 0)
    for i in range(M): y, c1, c2, c3, c4 = map(int, input().split()); add(c1, i+N, 1, -4*y); add(c2, i+N, 1, -4*y+1); add(c3, i+N, 1, -4*y+2); add(c4, i+N, 1, -4*y+3)
    for i in range(M): add(i+N, t, 1, 0)
    while flow < k:
        id, d, q, p, pe = [0]*n, [INF]*n, [0]*n, [0]*n, [0]*n; qh = qt = 0; q[qt] = s; qt += 1; d[s] = 0
        while qh != qt:
            v = q[qh]; qh += 1; id[v] = 2
            if qh == n: qh = 0
            for i in range(len(al[v])):
                r = el[al[v][i]]
                if r[4] < r[2] and d[v]+r[3] < d[r[1]]:
                    d[r[1]] = d[v]+r[3]
                    if id[r[1]] == 0:
                        q[qt] = r[1]; qt += 1
                        if qt == n: qt = 0
                    elif id[r[1]] == 2:
                        qh -= 1
                        if qh == -1: qh = n-1
                        q[qh] = r[1]
                    id[r[1]] = 1; p[r[1]] = v; pe[r[1]] = i
        if d[t] == INF: break
        addflow, v = k-flow, t
        while v != s: ee = al[p[v]][pe[v]]; addflow = min(addflow, el[ee][2]-el[ee][4]); v = p[v]
        v = t
        while v != s: ee = al[p[v]][pe[v]]; el[ee][4] += addflow; el[al[v][el[ee][5]]][4] -= addflow; cost += el[ee][3]*addflow; v = p[v]
        flow += addflow
    print(-cost)