N = int(input()); G = [[] for _ in range(N)]; B = [0]*N
for _ in range(N-1): a, b, w = map(int, input().split()); a -= 1; b -= 1; G[a] += [(b, w)]; G[b] += [(a, w)]
for _ in range(int(input())): a, b = map(int, input().split()); B[a-1] ^= 1; B[b-1] ^= 1
Q = [(0, -1, 0, 0)]; Z = 0
while Q:
    u, p, w, b = Q.pop()
    if b:
        for v, _ in G[u]:
            if v != p: B[u] ^= B[v]
        if B[u]: Z += w
    else:
        Q += [(u, p, w, 1)]
        for v, w in G[u]:
            if v != p: Q += [(v, u, w, 0)]
print(Z)