import sys; input = sys.stdin.readline
M = 10**9+7; P = 31; P2 = 29; I = pow(P, -1, M); I2 = pow(P2, -1, M); L = 16; W = []; C = []
while (s:=input().strip()): W.append(s+'{'*(L-len(s))); C.append(s)
r = {e:i for i,e in enumerate(W)}; T = []; N = len(W); G = [[] for _ in range(N)]
for w in W:
    p = [0]; p2 = [0]; h = []
    for j in w: p.append((p[-1]*P+ord(j)-97)%M); p2.append((p2[-1]*P2+ord(j)-97)%M)
    for j in range(L): h.append(((p[-1]-(ord(w[j])-97-(I-1)*p[j]*P)*pow(P, L-1-j, M))%M, (p2[-1]-(ord(w[j])-97-(I2-1)*p[j]*P2)*pow(P2, L-1-j, M))%M))
    T.append(h)
for i in range(L):
    k = {}
    for j in range(N):
        if T[j][i] not in k: k[T[j][i]] = []
        k[T[j][i]].append(j)
    for j in k.values():
        for m in range(len(j)):
            for n in range(m+1, len(j)):
                if len(C[j[m]]) == len(C[j[n]]): G[j[m]].append(j[n]); G[j[n]].append(j[m])
while (s:=input().strip()):
    a, b = s.split(); a = r[a+'{'*(L-len(a))]; b = r[b+'{'*(L-len(b))]; Z = [-1]*N; Q = [(a, N)]
    for u, p in Q:
        if Z[u] != -1: continue
        Z[u] = p
        for v in G[u]:
            if v != p: Q.append((v, u))
    if Z[b] == -1: print('No solution.')
    else:
        z = []; c = b
        while c != N: z.append(c); c = Z[c]
        while z: print(W[z.pop()].strip('{'))
    print()