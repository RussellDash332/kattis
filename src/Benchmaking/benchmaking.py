import sys; input = sys.stdin.readline
M = {}; V = []; G = [{} for _ in range(10**4)]
for _ in range(int(input())):
    input(); c, x = input().split(); c = int(c)
    if x not in M: M[x] = len(M); V.append(x)
    for _ in range(int(input())):
        d, y = input().split(); d = int(d)
        if y not in M: M[y] = len(M); V.append(y)
        G[M[x]][M[y]] = (d, c)
input(); T = []; Q = {}
for _ in range(int(input())):
    c, x = input().split(); c = int(c)
    if x not in M: M[x] = len(M); V.append(x)
    if M[x] not in Q: Q[M[x]] = 0
    Q[M[x]] += c
N = len(M); I = [0]*N
for i in range(N):
    for j in G[i]: I[j] += 1
D = [i for i in range(N) if I[i] == 0]; Z = [0]*N
for k, v in Q.items(): Z[k] = v
for u in D:
    T.append(u)
    for v in G[u]: I[v] -= 1; I[v] < 1 and D.append(v)
for u in T:
    for v, (d, c) in G[u].items(): Z[v] += (Z[u]+c-1)//c*d
    if not G[u] and Z[u]: print(Z[u], V[u])