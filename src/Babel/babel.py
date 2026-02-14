import sys; input = sys.stdin.readline
class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]
K = ((0, -1), (-1, 0), (1, 0), (0, 1))
R, C = map(int, input().split())
M = [input() for _ in range(R)]
U = UFDS(R*C)
for r in range(R):
    for c in range(C):
        for i, j in K:
            if R>r+i>-1<c+j<C and M[r][c]==M[r+i][c+j]: U.union(r*C+c, (r+i)*C+c+j)
for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    if U.find(a*C+b) == U.find(x*C+y): print(M[a][b])
    else: print('N')