import sys; input = sys.stdin.readline
N, M = map(int, input().split()); P = [0]*N; G = [[] for _ in range(N)]
for _ in range(N-1): a, b = map(int, input().split()); P[b-1] = a-1; G[a-1].append(b-1)
for i in range(N): G[i].sort(reverse=True)

t = 0; T = [-1]*N; U = [-1]*N; s = [0]
while s:
    ub = s.pop()
    u, b = ub//2, ub%2
    if b: U[u] = t
    else:
        s.append(2*u+1); T[u] = t; t += 1
        for v in G[u]: s.append(2*v)

H = -1
for i in range(M):
    q = int(input())-1
    if U[q] <= H: print(i), exit(0)
    H = max(H, T[q])
print(M)