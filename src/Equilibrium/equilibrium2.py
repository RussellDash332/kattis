import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**5)
N = int(input()); G = [[] for _ in range(N)]; T = [[] for _ in range(N)]; V = set()
for _ in range(N-1): a, b = map(int, input().split()); G[a].append(b); G[b].append(a)
Q = [(0, -1)]
while Q:
    u, p = Q.pop()
    if u in V: continue
    V.add(u); Q.extend((v, u) for v in G[u])
    if ~p: T[p].append(u)
def f(v, p):
    for i in range(n:=min(len(T[v])//2+p, len(T[v]))): f(T[v][i], 1)
    print(v, end=' ')
    for i in range(n, len(T[v])): f(T[v][i], 0)
f(0, 0)