import sys; input = sys.stdin.readline; from collections import *; INF = 10**8
A, F = map(int, input().split()); R, C = map(int, input().split()); M = [input().strip() for _ in range(R)]; D = [[INF]*C for _ in range(R)]; E = [[INF]*C for _ in range(R)]; G = [[] for _ in range(1005)]; T = [[] for _ in range(1005)]; H = {}; N = []
for i in range(R*C):
    if M[i//C][i%C] == 'S': si, sj = i//C, i%C; D[si][sj] = E[si][sj] = 0
    if M[i//C][i%C] == 'G': gi, gj = i//C, i%C
    if M[i//C][i%C] != 'B': H[(i//C, i%C)] = len(H); N.append((i//C, i%C))
for i in range(len(N)):
    r, c = N[i]
    for j in range(i+1, len(N)):
        rr, cc = N[j]
        if (r-rr)**2+(c-cc)**2 <= A*A: G[i].append(j); G[j].append(i)
        if (r==rr and abs(c-cc)<=F) or (c==cc and abs(r-rr)<=F): T[i].append(j); T[j].append(i)
q = deque([(si, sj)])
while q:
    r, c = q.popleft()
    if r == gi and c == gj: break
    for i in G[H[(r, c)]]:
        nr, nc = N[i]
        if D[nr][nc] == INF: D[nr][nc] = D[r][c]+1; q.append((nr, nc))
if D[gi][gj] == INF: print('NO WAY'), exit(0)
q = deque([(si, sj)])
while q:
    r, c = q.popleft()
    if r == gi and c == gj: break
    for i in T[H[(r, c)]]:
        nr, nc = N[i]
        if E[nr][nc] == INF: E[nr][nc] = E[r][c]+1; q.append((nr, nc))
x = D[gi][gj]; y = E[gi][gj]
if x == y: print('SUCCESS')
elif x < y: print('GO FOR IT')
else: print('NO CHANCE')