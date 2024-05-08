import sys; input = sys.stdin.readline; from heapq import *
R, C = map(int, input().split()); M = [[*map(int, input().split())] for _ in range(R)]; T = [x.copy() for x in M]; S = [[0]*C for _ in range(R)]
Di, Dj = map(int, input().split()); Q = [(M[Di-1][Dj-1], Di-1, Dj-1)]; A = 0; S[Di-1][Dj-1] = 1; K = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
while Q:
    v, r, c = heappop(Q); A -= v
    for dr, dc in K:
        if R>r+dr>-1<c+dc<C:
            if T[r+dr][c+dc] < v: T[r+dr][c+dc] = v
            if M[r+dr][c+dc] <= T[r+dr][c+dc] < 0 == S[r+dr][c+dc]: heappush(Q, (T[r+dr][c+dc], r+dr, c+dc)); S[r+dr][c+dc] = 1
print(A)