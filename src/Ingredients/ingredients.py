import sys; input = sys.stdin.readline
B = int(input())
R = {}
E = []
for _ in range(int(input())):
    d, b, a, c, p = input().split()
    c = int(c); p = int(p)
    if d not in R: R[d] = len(R)
    if b not in R: R[b] = len(R)
    if a not in R: R[a] = len(R)
    E.append((R[d], R[b], R[a], c, p))
N = len(R)
G = [[] for _ in range(N)]
I = [0]*N
C = [0]*N
P = [0]*N
S = set()
for d, b, a, c, p in E:
    I[b] += 1; I[a] += 1; G[d] += [(b, a, c, p)]; S.add(d)
Q = [u for u in range(N) if I[u]<1]
for d in Q:
    for b, a, _, _ in G[d]:
        I[b] -= 1; I[a] -= 1
        if I[b]<1: Q.append(b)
        if I[a]<1: Q.append(a)
for d in Q[::-1]:
    if not G[d]: continue
    x = y = 10**18
    for b, a, c, p in G[d]: x, y = min((x, y), (C[b]+C[a]+c, -P[b]-P[a]-p))
    C[d] = x; P[d] = -y
Z = [0]*-~B; T = 0
for i in S:
    c = C[i]; p = P[i]; T += c
    for j in range(min(B, T)-c, -1, -1): Z[j+c] = max(Z[j+c], Z[j]+p)
m, n = max((Z[i], -i) for i in range(B+1))
print(m, -n)