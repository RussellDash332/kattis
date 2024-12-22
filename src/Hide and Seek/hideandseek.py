from array import *
m, n = map(int, input().split()); G = [{} for _ in range(m)]; V = [0]*m; S = [(0, -1)]; T = [array('b') for _ in range(m)]
for _ in range(m-1): a, b, t = map(int, input().split()); G[a][b] = G[b][a] = t
while S:
    u, p = S.pop()
    if V[u]: continue
    V[u] = 1
    if p != -1: T[p].append(u)
    S.extend((v, u) for v in G[u] if u != p)
L = max(map(len, T)); H = array('b', [-1]*(L*m*(n+1)*2))
def f(x, y, t, c):
    if y == len(T[x]) or t == 0: return 1
    if H[(k:=(2*((n+1)*(L*x+y)+t)+c))] > -1: return H[k]
    A = 0; C = G[x][(Z:=T[x][y])]
    if c:
        ti = C
        while ti <= t:  A = max(A, f(Z, 0, ti-C, c)+f(x, y+1, t-ti, 0)); ti += 1
    ti = 2*C
    while ti <= t:      A = max(A, f(Z, 0, ti-2*C, 0)+f(x, y+1, t-ti, c)); ti += 1
    A = max(A, f(x, y+1, t, c)) # skip visiting to the y-th child of x)
    H[k] = A; return A
print(f(0, 0, n, 1)-1)