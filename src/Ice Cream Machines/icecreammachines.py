import sys; input = sys.stdin.readline; from heapq import *
N, M, K = map(int, input().split()); F = [[] for _ in range(M)]; S = []; Q = []; T = [0]*M; A = Z = 0
for i in range(N): f = int(input())-1; F[f].append(i); S.append(f)
for f in F: f.append(N); f.reverse(); f.pop()
for f in S:
    while (x:=1-T[f]) and Z==K: j = heappop(Q)%M; Z -= T[j]; T[j] = 0
    heappush(Q, -F[f].pop()*M+f); A += x; Z += x; T[f] = 1
print(A)