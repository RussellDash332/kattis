import sys; input = sys.stdin.readline
n, k = map(int, input().split())
c = {(i, j) for i in range(k) for j in range(k)}
for _ in range(n):
    s = input().strip()
    for i in range(k):
        for j in range(i+1): c.discard((ord(s[i])-65, ord(s[j])-65))
G = [[] for _ in range(k)]; D = [0]*k
for a, b in c: G[a].append(b); D[b] += 1
T = []; Q = [i for i in range(k) if D[i] == 0]; Z = [1]*k
for u in Q:
    T.append(u)
    for v in G[u]:
        D[v] -= 1
        if D[v] == 0: Q.append(v)
while T:
    u = T.pop()
    for v in G[u]: Z[u] = max(Z[u], Z[v]+1)
print(max(Z))