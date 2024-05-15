import sys; input = sys.stdin.readline
V, E = map(int, input().split()); G = [set() for _ in range(V)]; M = 10**9
for _ in range(E): a, b = map(int, input().split()); G[a].add(b); G[b].add(a)
for i in range(V):
    for j in G[i]:
        for k in G[j]:
            if i in G[k]: print(3); exit(0)
for i in range(V):
    S = [0]*V; Q = [(i, -1, 1)]
    for u, p, d in Q:
        if d >= M: break
        if S[u]: M = min(M, d+S[u]-2); break
        S[u] = d
        for v in G[u]:
            if v != p: Q.append((v, u, d+1))
print(M if M < 10**9 else 'impossible')