import sys; input = sys.stdin.readline
G = {}
for _ in '.'*int(input()):
    c, k = input().split(); z = []
    for _ in '.'*int(k):
        v, u = input().strip().split(); z.append((u, int(v)))
    G[c] = z
Z = {}; Q = [(input().strip(), 1)]
for u, d in Q:
    if u not in G: Z[u] = Z.get(u, 0)+d; continue
    for v, k in G[u]: Q.append((v, k*d))
for k in sorted(Z): print(k, Z[k])