import sys; input = sys.stdin.readline
from collections import deque
R, C = map(int, input().split())
B = [input().strip() for _ in range(R)]
A = [[0]*C for _ in range(R)]
K = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
D = ((1, 0), (0, 1), (0, -1), (-1, 0))
for i in range(R):
    for j in range(C):
        if B[i][j] == 'R': S = C*i+j
        if B[i][j] == 'K':
            for dr, dc in K:
                if 0<=i+dr<R and 0<=j+dc<C: A[i+dr][j+dc] += 1
Q = deque([S])
vis = set()
while Q:
    u = Q.popleft()
    r, c = u//C, u%C
    if B[r][c] == 'T': print('yes'), exit(0)
    if B[r][c] == 'K':
        for dr, dc in K:
            if 0<=r+dr<R and 0<=c+dc<C:
                A[r+dr][c+dc] -= 1
                if A[r+dr][c+dc] == 0:
                    m = C*(r+dr)+c+dc
                    for rr, cc in D:
                        pr, pc = r+dr+rr, c+dc+cc
                        while 0<=pr<R and 0<=pc<C:
                            if C*pr+pc in vis and m not in vis: vis.add(m), Q.append(m)
                            elif B[pr][pc] == 'K': break
                            pr += rr; pc += cc
    for rr, cc in D:
        pr, pc = r+rr, c+cc
        m = C*pr+pc
        while 0<=pr<R and 0<=pc<C:
            if m not in vis:
                if A[pr][pc] == 0: vis.add(m), Q.append(m)
                if B[pr][pc] == 'K': break
            else: break
            pr += rr; pc += cc; m += C*rr+cc
print('no')