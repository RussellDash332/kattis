import sys; input = sys.stdin.readline

n, c, s, f = map(int, input().split()); s -= 1
S = input().strip()
F = {*map(lambda x: int(x)-1, input().split()), n}
T = [[*map(lambda x: int(x)-1, input().split())] for _ in range(n)]

G = [[] for _ in range(n)]+[[s]]
for i in F: G[i].append(n)

def eclose(s):
    Q = [i for i in range(n+1) if s&(1<<i)]; S = 0
    for u in Q:
        if S&(1<<u): continue
        S |= 1<<u; Q.extend(G[u])
    return S

def can(s):
    return any(s&1<<i for i in F)

H = {}; L = []; Z = []; Q = []
s = eclose(1<<n)
H[s] = len(H); L.append(s); Q.append(H[s]); M = [[0]*c]; Z.append(can(s))
for u in Q:
    curr = L[u]
    for v in range(c):
        nxt = 0
        for i in range(n):
            if curr&(1<<i): nxt |= 1<<T[i][v]
        nxt = eclose(nxt)
        if nxt not in H:
            H[nxt] = len(H); L.append(nxt); Q.append(H[nxt]); M.append([0]*c); Z.append(can(nxt))
        M[u][v] = H[nxt]+1
n = len(Z); F = [i+1 for i in range(n) if Z[i]]

print(n, c, 1, len(F))
print(S)
print(*sorted(F))
for r in M: print(*r)