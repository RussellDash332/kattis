import sys; input = sys.stdin.readline
class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N; s.s = [0]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x; s.s[x] += s.s[y]
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]; s.s[y] += s.s[x]
R, C = map(int, input().split()); M = [input() for _ in range(R)]; K = ((-1, 0), (0, -1), (0, 1), (1, 0)); U = UFDS(R*C); Z = {}
for i in range(R):
    for j in range(C): U.s[C*i+j] = int(M[i][j] == '*')
for i in range(R):
    for j in range(C):
        for di, dj in K:
            if M[i][j] in ' *' and R>i+di>-1<j+dj<C and M[i+di][j+dj] in ' *': U.union(C*i+j, C*(i+di)+j+dj)
for i in range(R):
    for j in range(C):
        if M[i][j] in ' *': Z[s] = U.s[s:=U.find(C*i+j)]
print(len(Z), max(Z.values()))