N, T = map(int, input().split()); E = []; K = []; P = [10**18]*-~N; Q = [10**18]*T; z = 10**18; P[1] = 0
for i in range(T): u, v, d, a = map(int, input().split()); E += [(d, 1, i), (a, 0, i)]; K += [(u, v)]
for t, c, i in sorted(E):
    u, v = K[i]
    if c:
        if P[u] < 10**18: Q[i] = P[u]+t
    else:
        if Q[i] < 10**18:
            P[v] = min(P[v], Q[i]-t)
            if v == N: z = min(z, Q[i])
print(z if z<10**18 else -1)