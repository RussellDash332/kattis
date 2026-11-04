N, M = map(int, input().split()); Z = 0
G = [[] for _ in range(N)]; K = N
for _ in range(M): a, b = map(int, input().split()); G[a-1] += [b-1]; G[b-1] += [a-1]
for i in range(N):
    D = [N]*N; D[i] = C = 0; Q = [i]; W = [0]*N; W[i] = 1; B = K+1
    for u in Q:
        if W[u] > 1:
            x = 2*D[u]
            if x <= K:
                c = W[u]*~-W[u]//2
                if x < B: B = x; C = c
                elif x == B: C += c
        for v in G[u]:
            if D[u] == D[v]:
                if u < v:
                    x = 2*D[u]+1
                    if x <= K:
                        c = W[u]*W[v]
                        if x < B: B = x; C = c
                        elif x == B: C += c
            elif D[u]+1 < D[v]: D[v] = D[u]+1; Q += [v]; W[v] = W[u]
            elif D[u]+1 == D[v]: W[v] += W[u]
    if B < K: K = B; Z = C
    elif B == K: Z += C
print(Z//K)