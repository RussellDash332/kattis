from collections import *
R, C, x, y = map(int, input().split()); m = [input() for _ in '.'*R]; q = deque([(x:=x-1, y:=y-1, 0)]); f = (q.appendleft, q.append, q.append); K = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]; V = set()
while q:
    r, c, d = q.popleft(); k = int(m[r][c])-1
    if (r, c) in V:
        if (r, c) == (x, y): print(d)<exit()
        continue
    V.add((r, c))
    for i in (-1, 0, 1):
        dr, dc = K[(k+i)%8]
        if R>r+dr>-1<c+dc<C and m[r+dr][c+dc]>'#': f[i]((r+dr, c+dc, d+abs(i)))