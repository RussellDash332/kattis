import sys; input = sys.stdin.readline; P = []; C = []; N = int(input())
for _ in range(N): c, *p = map(lambda x: int(x)-1, input().split()); P.append(p); C.append(c+1)

def solve(CNF):
    G = [[] for _ in range(2*N)]; Gt = [[] for _ in range(2*N)]; T, V, S = [], [0]*2*N, 1
    for (a, p), (b, q) in CNF: G[a+N*(1-p)].append(b+N*q); G[b+N*(1-q)].append(a+N*p)
    for i in range(2*N):
        for j in G[i]: Gt[j].append(i)
    def DFS(s, t):
        U = [2*s]; a = G if t else Gt
        while U:
            ub = U.pop()
            u, b = ub//2, ub%2
            if b and t: T.append(u)
            elif V[u] == 0:
                V[u] = S; U.append(2*u+1)
                for v in a[u]:
                    if V[v] == 0: U.append(2*v)
        return 1
    for i in range(2*N):
        if V[i] == 0: DFS(i, 1)
    V = [0]*2*N
    for i in T[::-1]:
        if V[i] == 0: S += DFS(i, 0)
    return not any(V[i]==V[i+N] for i in range(N))

def f(t):
    CNF = []
    for i in range(N):
        for j in range(t, N-1):
            if C[i] == C[P[i][j]]: CNF.append(((i, 0), (P[i][j], 0))); CNF.append(((i, 1), (P[i][j], 1)))
            elif (C[i]-C[P[i][j]])%3 == 1: CNF.append(((i, 1), (P[i][j], 0)))
            else: CNF.append(((i, 0), (P[i][j], 1)))
    return solve(CNF)

lo, hi = 0, N-1
while lo < hi:
    if f(mi:=(lo+hi)//2): hi = mi
    else: lo = mi+1
print(lo)