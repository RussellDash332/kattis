import sys; input = sys.stdin.readline
N, M = map(int, input().split())
P = [[*map(int, input().split())] for _ in range(N)]
G = [[] for _ in range(N)]; D = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a] += [b]; G[b] += [a]; D[a] += 1; D[b] += 1
R = {}; T = [set() for _ in range(N)]; I = [0]*N
Q = [i for i in range(N) if D[i]<=5]
for i in Q: I[i] = 1
for u in Q:
    R[u] = len(R)
    for v in G[u]:
        D[v] -= 1
        if D[v]<=5 and I[v]<1: I[v] = 1; Q += [v]
for u in range(N):
    for v in G[u]:
        if R[u]<R[v]: T[u].add(v)
Z = 5; S = set()
for i in range(N):
    for a in T[i]:
        if T[a]&T[i]: print(3); exit() # x<-i->a->x
    for a in T[i]:
        for b in T[i]:
            if a < b:
                if T[a]&T[b]: Z = 4 # x<-b<-i->a->x
                if (a, b) in S: Z = 4 # i->a<-j->b<-i
                S.add((a, b))
        for b in T[a]:
            if T[b]&T[i]: Z = 4 # i->a->b->x<-i
print(Z)