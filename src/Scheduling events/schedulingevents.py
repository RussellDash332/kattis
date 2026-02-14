import sys; input = sys.stdin.readline
N, K = map(int, input().split())
P = [p:=0]+[p:=p+i for i in map(int, input().split())]
L = [*map(int, input().split())]
if sum(L)>N: print(-1); exit()
D = [0]*(N+1); S = 0
for i in range(1, K+1):
    E = [10**9]*(N+1); T = 10**9
    for j in range(S+L[i-1], N+1): T = min(T, D[j-L[i-1]]); E[j] = min(E[j-1], T+P[j]-P[j-L[i-1]])
    S += L[i-1]; D = E
print(D[N])