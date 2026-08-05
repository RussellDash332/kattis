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

# [(-40, 0), (40, 0)]
N = int(input()); U = UFDS(N+2); R = 40; r = 25
C = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    x1, y1 = C[i]
    for j in range(N):
        x2, y2 = C[j]
        if (x2-x1)**2 + (y2-y1)**2 < 4*(R+r)**2: U.union(i, j)
    if y1 < R+2*r:
        if x1 <= -R: U.union(i, N)
        if x1 >= R: U.union(i, N+1)
print('im'*(U.find(N)==U.find(N+1))+'possible')