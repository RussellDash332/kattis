B = [[*input()] for _ in range(8)]
up = lambda s: s.isupper()
low = lambda s: s.islower()

def get(i, j):
    res = []; pc = B[i][j]; F, G = up, low
    if up(pc): F, G = G, F
    if pc in 'Pp':
        d = low(pc)-up(pc)
        if not 8>i+d>-1: return res
        if B[i+d][j] == '.':
            res.append((i+d, j))
            if i == (1, 6)[up(pc)] and B[i+2*d][j] == '.': res.append((i+2*d, j))
        if j-1 >= 0 and F(B[i+d][j-1]): res.append((i+d, j-1))
        if j+1 < 8 and F(B[i+d][j+1]): res.append((i+d, j+1))
    if pc in 'Nn':
        for di, dj in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
            if 8>i+di>-1<j+dj<8 and not G(B[i+di][j+dj]): res.append((i+di, j+dj))
    if pc in 'Kk':
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if (di or dj) and 8>i+di>-1<j+dj<8 and not G(B[i+di][j+dj]): res.append((i+di, j+dj))
    if pc in 'BQbq':
        for di in (-1, 1):
            for dj in (-1, 1):
                for k in range(1, 8):
                    if not 8>i+k*di>-1<j+k*dj<8: break
                    if G(B[i+k*di][j+k*dj]): break
                    res.append((i+k*di, j+k*dj))
                    if F(B[i+k*di][j+k*dj]): break
    if pc in 'RQrq':
        for r in (range(1, 8), range(-1, -8, -1)):
            for k in r:
                if not 8>i+k>-1: break
                if G(B[i+k][j]): break
                res.append((i+k, j))
                if F(B[i+k][j]): break
            for k in r:
                if not 8>j+k>-1: break
                if G(B[i][j+k]): break
                res.append((i, j+k))
                if F(B[i][j+k]): break
    return res

def check(f):
    for i in range(8):
        for j in range(8):
            if f(B[i][j]):
                for r, c in get(i, j):
                    if B[r][c] == 'Kk'[f==up]: return 1
    return 0

for i in range(8):
    for j in range(8):
        if up(B[i][j]):
            for r, c in get(i, j):
                os, od = B[i][j], B[r][c]; prw = os
                if os == 'P' and r == 0: prw = 'NQBR'
                for pr in prw:
                    B[i][j], B[r][c] = '.', pr
                    if check(up) and not check(low):
                        cm = 1
                        for ii in range(8):
                            for jj in range(8):
                                if low(B[ii][jj]):
                                    for rr, cc in get(ii, jj):
                                        oss, odd = B[ii][jj], B[rr][cc]; prb = oss
                                        if oss == 'p' and rr == 7: prb = 'nqbr'
                                        for prr in prb: B[ii][jj], B[rr][cc] = '.', prr; cm &= check(up); B[ii][jj], B[rr][cc] = oss, odd
                        if cm: print(chr(j+97)+str(8-i)+chr(c+97)+str(8-r)); exit()
                    B[i][j], B[r][c] = os, od