import sys
INF = 1e18
P, R, _ = map(int, input().split())
s, t, n = R, R+2, R+3
al, el, k = [[] for _ in range(n)], [], INF

def add_edge(u, v, c=1, w=1):
    e1, e2 = [u, v, c, w, 0, len(al[v])], [v, u, 0, -w, 0, len(al[u])]
    al[u].append(len(el)), el.append(e1), al[v].append(len(el)), el.append(e2)

add_edge(s, -2, P, 0)
for _ in sys.stdin:
    e1, e2 = map(int, _.split())
    add_edge(e1, e2), add_edge(e2, e1)

flow = cost = 0
while flow < k:
    id, d, q, p, pe = [0]*n, [INF]*n, [0]*n, [0]*n, [0]*n
    qh = qt = 0
    q[qt] = s; qt += 1
    d[s] = 0
    while qh != qt:
        v = q[qh]; qh += 1
        id[v] = 2
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
    while v != s:
        ee = al[p[v]][pe[v]]
        addflow = min(addflow, el[ee][2]-el[ee][4])
        v = p[v]
    v = t
    while v != s:
        ee = al[p[v]][pe[v]]
        el[ee][4] += addflow
        el[al[v][el[ee][5]]][4] -= addflow
        cost += el[ee][3]*addflow
        v = p[v]
    flow += addflow
if flow < P: print(f'{P-flow} people left behind')
else: print(cost)