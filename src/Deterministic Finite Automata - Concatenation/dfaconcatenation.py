import sys; input = sys.stdin.readline

n1, c1, s1, f1 = map(int, input().split()); s1 -= 1
S1 = input().strip()
F1 = [*map(lambda x: int(x)-1, input().split())]
T1 = [[*map(lambda x: int(x)-1, input().split())] for _ in range(n1)]

n2, c2, s2, f2 = map(int, input().split()); s2 -= 1
S2 = input().strip()
F2 = [*map(lambda x: int(x)-1, input().split())]
T2 = [[*map(lambda x: int(x)-1, input().split())] for _ in range(n2)]

# S1 == S2 so c1 == c2
n = n1+n2
T = [[0]*c1 for _ in range(n)]
for i in range(c1):
    for j in range(n1): T[j][i] = T1[j][i]
    for j in range(n2): T[n1+j][i] = T2[j][i]+n1

G = [[] for _ in range(n)]
for f in F1: G[f].append(s2+n1)

def eclose(s):
    Q = [i for i in range(n) if s&(1<<i)]; S = 0
    for u in Q:
        if S&(1<<u): continue
        S |= 1<<u; Q.extend(G[u])
    return S

def can(s):
    return any(s&1<<(n1+f) for f in F2)

H = {}; L = []; Z = []; Q = []
s = eclose(1<<s1)
H[s] = len(H); L.append(s); Q.append(H[s]); M = [[0]*c1]; Z.append(can(s))
for u in Q:
    curr = L[u]
    for v in range(c1):
        nxt = 0
        for i in range(n):
            if curr&(1<<i): nxt |= 1<<T[i][v]
        nxt = eclose(nxt)
        if nxt not in H:
            H[nxt] = len(H); L.append(nxt); Q.append(H[nxt]); M.append([0]*c1); Z.append(can(nxt))
        M[u][v] = H[nxt]+1
n = len(Z); F = [i+1 for i in range(n) if Z[i]]

print(n, c1, 1, len(F))
print(S1)
print(*F)
for r in M: print(*r)