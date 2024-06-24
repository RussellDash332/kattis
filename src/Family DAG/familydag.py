import sys; input = sys.stdin.readline
R = {}; G = []; X = []; V = ('hillbilly', 'paradox', 'paradox')
while True:
    s = input().strip()
    if not s: break
    if s != 'done':
        a, _, b = s.split()
        if a not in R: R[a] = len(R); G.append([]); X.append(a)
        if b not in R: R[b] = len(R); G.append([]); X.append(b)
        G[R[b]].append(R[a])
        continue
    N = len(R); Z = [0]*N
    for i in range(N):
        # DFS from i as source, if got multiple visits, gets a report
        s = [i]; v = [0]*N
        while s:
            u = s.pop()
            if v[u]: Z[i] |= 1<<(u==i); continue
            v[u] = 1; s.extend(G[u])
    for i in sorted(R):
        if Z[R[i]]: print(i, V[Z[R[i]]-1])
    R = {}; G = []; print()