# bit lazy for full marks ;)
class State:
    def __init__(self, B, z='', g=0):
        self.B = tuple(B)
        self.z = z # history
        self.g = g # cost
        self.h = 0 # heuristic
        for i in range(n):
            for j in range(m):
                self.h += abs((B[i*m+j]-1)//m-i)+abs(((B[i*m+j]-1)%m-j))
                if B[i*m+j] == n*m: self.p = (i, j)
    def __lt__(self, other):
        return self.g+self.h < other.g+other.h
    def next(self):
        i, j = self.p; nxt = []; nc = self.g+2
        if i > 0 and (not self.z or self.z[-1] != 'U'): C = [*self.B]; C[i*m+j], C[(i-1)*m+j] = C[(i-1)*m+j], C[i*m+j]; nxt.append(State(C, self.z+'D', nc))
        if i < n-1 and (not self.z or self.z[-1] != 'D'): C = [*self.B]; C[i*m+j], C[(i+1)*m+j] = C[(i+1)*m+j], C[i*m+j]; nxt.append(State(C, self.z+'U', nc))
        if j > 0 and (not self.z or self.z[-1] != 'L'): C = [*self.B]; C[i*m+j], C[i*m+j-1] = C[i*m+j-1], C[i*m+j]; nxt.append(State(C, self.z+'R', nc))
        if j < m-1 and (not self.z or self.z[-1] != 'R'): C = [*self.B]; C[i*m+j], C[i*m+j+1] = C[i*m+j+1], C[i*m+j]; nxt.append(State(C, self.z+'L', nc))
        return nxt
    def __repr__(self):
        return str([[self.B[i*m+j] for j in range(m)] for i in range(n)])

from heapq import *
n, m = map(int, input().split()); seen = {}; B = []
for _ in range(n): B.extend(map(int, input().split()))
pq = [State(B)]
while pq:
    st = heappop(pq)
    if st.h == 0: print(st.z); exit()
    for nxt in st.next():
        if nxt.B not in seen or nxt.g < seen[nxt.B]: heappush(pq, nxt); seen[nxt.B] = nxt.g
print('impossible')