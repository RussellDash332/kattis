K = ((0, -1), (1, 0), (0, 1), (-1, 0))
R, C = map(int, input().split()); M = [input() for _ in range(R)]; V = [[0]*C for _ in range(R)]; X = 0
for i in range(R):
    for j in range(C):
        if M[i][j] in 'AB':
            s = [(i, j, 0, 0)]; x = ord(M[i][j])-67
            while s:
                r, c, dr, dc = s.pop()
                if V[r][c]: continue
                V[r][c] = x; t = []; n = 0
                for di, dj in K:
                    if R>r+di>-1<c+dj<C:
                        n += 1
                        if M[r+di][c+dj] == 'X': t.append((r+di, c+dj, di, dj))
                if len(t) == n and M[r][c] == 'X' and R>r+dr>-1<c+dc<C: V[r][c] = 0; t = [(r+dr, c+dc, dr, dc)]
                s.extend(t)
        else:
            if V[i][j] == 0 and M[i][j] == '.':
                s = [(i, j)]; X += 1
                while s:
                    r, c = s.pop()
                    if V[r][c]: continue
                    V[r][c] = X
                    for dr, dc in K:
                        if R>r+dr>-1<c+dc<C and M[r+dr][c+dc] == '.': s.append((r+dr, c+dc))
A = [[1]*C for _ in range(R)]; B = [[1]*C for _ in range(R)]
for i in range(R):
    for ii in (0, C-1):
        if A[i][ii] == 1 and V[i][ii] != -2 and V[i][ii] != 0:
            s = [(i, ii)]
            while s:
                r, c = s.pop()
                if A[r][c] == 0: continue
                A[r][c] = 0
                for dr, dc in K:
                    if R>r+dr>-1<c+dc<C and V[r+dr][c+dc] != -2 and V[r+dr][c+dc] != 0: s.append((r+dr, c+dc))
        if B[i][ii] == 1 and V[i][ii] != -1 and V[i][ii] != 0:
            s = [(i, ii)]
            while s:
                r, c = s.pop()
                if B[r][c] == 0: continue
                B[r][c] = 0
                for dr, dc in K:
                    if R>r+dr>-1<c+dc<C and V[r+dr][c+dc] != -1 and V[r+dr][c+dc] != 0: s.append((r+dr, c+dc))
for i in range(C):
    for ii in (0, R-1):
        if A[ii][i] == 1 and V[ii][i] != -2 and V[ii][i] != 0:
            s = [(ii, i)]
            while s:
                r, c = s.pop()
                if A[r][c] == 0: continue
                A[r][c] = 0
                for dr, dc in K:
                    if R>r+dr>-1<c+dc<C and V[r+dr][c+dc] != -2 and V[r+dr][c+dc] != 0: s.append((r+dr, c+dc))
        if B[ii][i] == 1 and V[ii][i] != -1 and V[ii][i] != 0:
            s = [(ii, i)]
            while s:
                r, c = s.pop()
                if B[r][c] == 0: continue
                B[r][c] = 0
                for dr, dc in K:
                    if R>r+dr>-1<c+dc<C and V[r+dr][c+dc] != -1 and V[r+dr][c+dc] != 0: s.append((r+dr, c+dc))
a = b = c = 0
for i in range(R):
    for j in range(C): a += V[i][j]>0 and A[i][j]>0 and B[i][j]<1; b += V[i][j]>0 and B[i][j]>0 and A[i][j]<1; c += V[i][j]>0 and A[i][j]>0 and B[i][j]>0
print(a, b, c)