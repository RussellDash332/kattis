n, N = map(int, input().split()); P = []
for _ in range(N): i, t = input().split(); P.append((int(i)-1, t))

def ok(i, j, x, y):
    a, s = P[i]; b, t = P[j]
    for k in range(max(a, b), min(a+len(s), b+len(t))):
        if s[a+len(s)-1-k if x else k-a] != t[b+len(t)-1-k if y else k-b]: return False
    return True

CNF = []; K = (0, 1)
for i in range(N):
    for j in range(i):
        for x in K:
            for y in K:
                if not ok(i, j, x, y): CNF.append(((i, 1-x), (j, 1-y)))

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

if any(V[i]==V[i+N] for i in range(N)): print('Villa'); exit()

S = ['A']*n
for i in range(N):
    a, s = P[i]; b = V[i]>V[i+N]
    for j in range(len(s)): S[a+(j if b else len(s)-1-j)] = s[j]
print(''.join(S))