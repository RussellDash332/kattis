import sys; input = sys.stdin.readline
for _ in range(int(input())):
    N, E = map(int, input().split())
    V = [*map(int, input().split())]
    G = [[] for _ in range(N)]; I = [0]*N
    for _ in range(E): a, b, c = map(int, input().split()); G[a-1] += [(b-1, c)]; I[b-1] += 1
    T = [i for i in range(N) if I[i]<1]; P = [-1]*N; D = [0]*N
    for u in T:
        for v, _ in G[u]: I[v] -= 1; I[v]<1!=T.append(v)
    for u in T[::-1]:
        z = 0; p = -1
        for v, w in G[u]:
            if D[v]-w+V[v] > z: z = D[v]-w+V[v]; p = v
        D[u] = z; P[u] = p
    Z = D[0]+V[0]; U = [0]
    while ~P[U[-1]]: U += [P[U[-1]]]
    print(Z, len(U), *(i+1 for i in U))