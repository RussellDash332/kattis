import sys; input = sys.stdin.readline
class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N; self.size = [1]*N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x; self.size[x] += self.size[y]
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]; self.size[y] += self.size[x]
R = int(input())
C = int(input())
U = int(input())
D = UFDS(R*C)
K = ((0, -1), (0, 1), (-1, 0), (1, 0))
M = [[*input().strip()] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if M[i][j] == 'S': S = C*i+j
        if M[i][j] != '.':
            for di, dj in K:
                if 0<=i+di<R and 0<=j+dj<C and M[i+di][j+dj] != '.': D.union(C*i+j, C*(i+di)+j+dj)
print(D.size[D.find(S)])
for _ in range(U):
    i, j = map(int, input().split()); i -= 1; j -= 1; M[i][j] = '#'
    for di, dj in K:
        if 0<=i+di<R and 0<=j+dj<C and M[i+di][j+dj] != '.': D.union(C*i+j, C*(i+di)+j+dj)
    print(D.size[D.find(S)])