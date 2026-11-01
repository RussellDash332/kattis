n = int(input())
M, R, D = map(int, input().split()); M -= 1; R -= 1; D -= 1
g = [[] for _ in range(n)]
for _ in range(n-1): a, b = map(int, input().split()); a -= 1; b -= 1; g[a] += [b]; g[b] += [a]
Q = [M]; V = [n]*n; V[M] = 0
for u in Q:
    for v in g[u]:
        if V[v]>V[u]+1: V[v] = V[u]+1; Q += [v]
Q = [R]; W = [n]*n; W[R] = 0
for u in Q:
    for v in g[u]:
        if W[v]>W[u]+1: W[v] = W[u]+1; Q += [v]
x = V[R]; y = V[D]; z = W[D]
print((y+z-x)/2/z)