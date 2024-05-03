import sys; input = sys.stdin.readline

class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N; self.q = [set() for _ in range(N)]
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
                while self.q[y]: self.q[x].add(self.q[y].pop())
            else:
                self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]
                while self.q[x]: self.q[y].add(self.q[x].pop())

N, M, Q = map(int, input().split()); U = UFDS(N+1)
for i in range(M): a, b = map(int, input().split()); U.q[a].add(i); U.q[b].add(i)
for _ in range(Q):
    a, b = map(int, input().split())
    if U.q[U.find(a)]&U.q[U.find(b)]: sys.stdout.write('REFUSE\n')
    else: U.union(a, b); sys.stdout.write('APPROVE\n')