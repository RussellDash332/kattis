N = int(input()); X = []; Y = []
for _ in range(N): x, y = map(int, input().split()); X.append(x); Y.append(y)

def possible(CNF):
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

def f(k):
    CNF = []
    for i in range(N):
        for j in range(i):
            if X[i]==X[j] and abs(Y[i]-Y[j]) <= 2*k: CNF.append(((i, 0), (j, 0))) # one must be vertical
            if Y[i]==Y[j] and abs(X[i]-X[j]) <= 2*k: CNF.append(((i, 1), (j, 1))) # one must be horizontal
    return possible(CNF)

lo, hi = 0, 10**6
while hi-lo>1:
    if f(mi:=(lo+hi)//2): lo = mi
    else: hi = mi-1
ans = hi if f(hi) else hi-1
print(ans if ans < 10**6 else 'UNLIMITED')