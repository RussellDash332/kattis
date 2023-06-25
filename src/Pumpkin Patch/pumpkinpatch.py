from collections import deque
p, d, n = map(int, input().split())
a, pk = [-1]*p, [[*map(int, input().split()), i] for i in range(p)]
v, q = [[-1]*n for _ in range(n)], deque([(*t, 0, -1) for t in pk])
delta, dd = ((0, 1), (1, 0), (0, -1), (-1, 0)), -1
debug = False
while q:
    if debug and dd < q[0][3]:
        for r in v:
            for i in r:
                if i == -1: print('.', end=' ')
                else: print(i, end=' ')
            print()
        print()
    r, c, idx, dd, dir = q.popleft()
    if a[idx] in [-1, dd] and dd <= d:
        if 0<=r<n and 0<=c<n:
            if v[r][c] == -1:
                v[r][c] = idx
                if dir == -1:
                    for i, (dr, dc) in enumerate(delta): q.append((r+dr, c+dc, idx, dd+1, i))
                else: dr, dc = delta[dir]; q.append((r+dr, c+dc, idx, dd+1, dir))
            else:
                a[idx] = dd
                if a[v[r][c]] == -1: a[v[r][c]] = dd
        else: a[idx] = dd
for i in a: print('ALIVE' if i == -1 else i)