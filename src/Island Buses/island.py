import sys; input = sys.stdin.readline
K = ((0, -1), (0, 1), (-1, 0), (1, 0)); T = 0
while True:
    M = [input().strip()]
    if not M[0]: break
    while True:
        M.append(input().strip())
        if not M[-1]: M.pop(); break
    R, C = len(M), len(M[0]); V = [[0]*C for _ in range(R)]; I = B = N = 0; T += 1
    for i in range(R):
        for j in range(C):
            if V[i][j]&1 == 0 and M[i][j] in '#X':
                s = [(i, j)]; I += 1
                while s:
                    r, c = s.pop()
                    if V[r][c]&1: continue
                    V[r][c] |= 1
                    for dr, dc in K:
                        if R>r+dr>-1<c+dc<C and M[r+dr][c+dc] in '#X': s.append((r+dr, c+dc))
            if V[i][j]&2 == 0 and M[i][j] == 'B':
                s = [(i, j)]; B += 1
                while s:
                    r, c = s.pop()
                    if V[r][c]&2: continue
                    V[r][c] |= 2
                    for dr, dc in K:
                        if R>r+dr>-1<c+dc<C and M[r+dr][c+dc] == 'B': s.append((r+dr, c+dc))
            if V[i][j]&4 == 0 and M[i][j] != '.':
                s = [(i, j)]; N += 1
                while s:
                    r, c = s.pop()
                    if V[r][c]&4: continue
                    V[r][c] |= 4
                    for dr, dc in K:
                        if R>r+dr>-1<c+dc<C and M[r+dr][c+dc] != '.':
                            if M[r][c] == 'B' and M[r+dr][c+dc] not in 'BX': continue
                            if M[r][c] == '#' and M[r+dr][c+dc] in 'B': continue
                            s.append((r+dr, c+dc))
    print('Map', T); print('islands:', I); print('bridges:', B); print('buses needed:', N); print()