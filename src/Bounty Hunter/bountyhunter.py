import sys; input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    P = sorted([*map(int, input().split())] for _ in range(N))
    P = [complex(x, y) for x, y in P]
    D = [[10**9]*N for _ in range(N)]
    D[0][1] = abs(P[0]-P[1])
    for j in range(2, N):
        for i in range(j):
            if i < j-1: D[i][j] = D[i][j-1]+abs(P[j-1]-P[j]); continue
            for k in range(j-1): D[i][j] = min(D[i][j], D[k][j-1]+abs(P[k]-P[j]))
    print(min(D[i][-1]+abs(P[i]-P[-1]) for i in range(N)))