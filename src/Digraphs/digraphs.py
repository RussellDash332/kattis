import sys; input = sys.stdin.readline
for _ in range(int(input())):
    G = [{*range(26)} for i in range(26)]; I = [0]*26; T = []
    for _ in range(int(input())): s = input(); a = ord(s[0])-97; b = ord(s[1])-97; G[a].discard(b)
    for i in range(26):
        for j in G[i]: I[j] += 1
    Q = [i for i in range(26) if I[i] == 0]
    for u in Q:
        T.append(u)
        for v in G[u]:
            I[v] -= 1
            if I[v] == 0: Q.append(v)
    if len(T) == 26:
        D = [(-1, -1) for _ in range(26)]
        while T:
            u = T.pop(); m = (0, -1)
            for v in G[u]: m = max(m, (D[v][0]+1, v))
            D[u] = m
        p = max(range(26), key=lambda x: D[x]); A = []
        while p != -1: A.append(p); p = D[p][1]
        if len(A)%2 == 0: A.pop()
    else:
        A = [None]
        def dfs(i, p):
            if A[0]: return
            p.append(i)
            if len(p) == 39: A[0] = [*p]; p.pop(); return
            for j in G[i]: dfs(j, p)
            p.pop()
        for i in range(26): dfs(i, [])
        A = A[0]
    N = len(A)//2+1
    for i in range(N): print(''.join(chr(A[i+j]+97) for j in range(N)))