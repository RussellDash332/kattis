N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a] += [b]; G[b] += [a]
S = [*map(int, input().split())]
T = [*map(int, input().split())]
V = [-1]*N; V[0] = 0; Q = [0]
if sum(S)-sum(T): print('NO'); exit()
for u in Q:
    for v in G[u]:
        if V[v] < 0: V[v] = V[u]^1; Q += [v]
        elif V[v] == V[u]: print('YES'); exit()
s = sum(S[i] for i in range(N) if V[i])
t = sum(T[i] for i in range(N) if V[i])
print('YNEOS'[s!=t and s!=sum(T)-t::2])