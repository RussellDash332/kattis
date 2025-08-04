import sys; input = sys.stdin.readline
N, M, K = map(int, input().split()); G = [[] for _ in range(N+K)]; I = [0]*(N+K)
for _ in range(M):
    n, k, c = input().strip().split(); n = int(n)-1; k = int(k)-1
    if c == 'A': G[n].append(k+N); I[k+N] += 1
    else: G[k+N].append(n); I[n] += 1
Q = [i for i in range(N+K) if I[i] == 0]; T = []
for u in Q:
    T.append(u)
    for v in G[u]: I[v] -= 1; I[v] < 1 and Q.append(v)
if len(T) != N+K: print(-1); exit()
for i in T: i < N and print(i+1, end=' ')