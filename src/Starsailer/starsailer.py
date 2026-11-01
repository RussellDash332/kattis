from heapq import *
N = int(input())
S = input()
T = input()
M = {}
G = [[] for _ in range(200)]
for _ in range(N):
    a, b, w = input().split()
    if a not in M: M[a] = len(M)
    if b not in M: M[b] = len(M)
    G[M[a]] += [(M[b], int(w))]
S = M[S]; T = M[T]; N = len(M); G = G[:N]
INF = float('inf'); D = [(INF, 0)]*N; D[S] = (0, 0); pq = [((0, 0), S)]
while pq:
    (dd, ss), vv = heappop(pq)
    if (dd, ss) != D[vv]: continue
    for nn, w in G[vv]:
        if D[nn] > (new:=(dd+w, ss+1)): D[nn] = new; heappush(pq, (new, nn))
print(max(D[T][1]-1, 0))