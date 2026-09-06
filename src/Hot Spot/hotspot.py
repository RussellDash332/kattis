m = [input() for _ in range(4)]
M = ['RGB.'.index(m[r][c]) for r in range(4) for c in range(4)]
K = 2**24-1
L = 2**16-1
N = ((-1, 0), (1, 0), (0, 1), (0, -1))
X = ((2, 2), (0, 2), (2, 0))
def f(b):
    G = [(b>>k)&3 for k in range(0, 32, 2)]
    z = []
    for r in range(4):
        if G[4*r+1] != 3 and G[4*r+2] != 3:
            if (i:=G[4*r]) != 3 and G[4*r+3] == 3:
                ok = 1
                for dr, dc in N:
                    if 4>r+dr>-1<3+dc<4 and (G[4*(r+dr)+3+dc], i) in X: ok = 0; break
                if ok: z.append(b-63*((3-i)<<(8*r)))
            if (i:=G[4*r+3]) != 3 and G[4*r] == 3:
                ok = 1
                for dr, dc in N:
                    if 4>r+dr>-1<dc<4 and (G[4*(r+dr)+dc], i) in X: ok = 0; break
                if ok: z.append(b+63*((3-i)<<(8*r)))
        if G[4+r] != 3 and G[8+r] != 3:
            if (i:=G[r]) != 3 and G[12+r] == 3:
                ok = 1
                for dr, dc in N:
                    if 4>3+dr>-1<r+dc<4 and (G[4*(3+dr)+r+dc], i) in X: ok = 0; break
                if ok: z.append(b-K*((3-i)<<(2*r)))
            if (i:=G[12+r]) != 3 and G[r] == 3:
                ok = 1
                for dr, dc in N:
                    if 4>dr>-1<r+dc<4 and (G[4*dr+r+dc], i) in X: ok = 0; break
                if ok: z.append(b+K*((3-i)<<(2*r)))
        if (i:=G[4*r]) != 3 and G[4*r+1] != 3 and G[4*r+2] == 3:
            ok = 1
            for dr, dc in N:
                if 4>r+dr>-1<2+dc<4 and (G[4*(r+dr)+2+dc], i) in X: ok = 0; break
            if ok: z.append(b-15*((3-i)<<(8*r)))
        if G[4*r] == 3 and G[4*r+1] != 3 and (i:=G[4*r+2]) != 3:
            ok = 1
            for dr, dc in N:
                if 4>r+dr>-1<dc<4 and (G[4*(r+dr)+dc], i) in X: ok = 0; break
            if ok: z.append(b+15*((3-i)<<(8*r)))
        if (i:=G[4*r+1]) != 3 and G[4*r+2] != 3 and G[4*r+3] == 3:
            ok = 1
            for dr, dc in N:
                if 4>r+dr>-1<3+dc<4 and (G[4*(r+dr)+3+dc], i) in X: ok = 0; break
            if ok: z.append(b-15*((3-i)<<(8*r+2)))
        if G[4*r+1] == 3 and G[4*r+2] != 3 and (i:=G[4*r+3]) != 3:
            ok = 1
            for dr, dc in N:
                if 4>r+dr>-1<1+dc<4 and (G[4*(r+dr)+1+dc], i) in X: ok = 0; break
            if ok: z.append(b+15*((3-i)<<(8*r+2)))
        if (i:=G[r]) != 3 and G[r+4] != 3 and G[r+8] == 3:
            ok = 1
            for dr, dc in N:
                if 4>2+dr>-1<r+dc<4 and (G[4*(2+dr)+r+dc], i) in X: ok = 0; break
            if ok: z.append(b-L*((3-i)<<(2*r)))
        if G[r] == 3 and G[r+4] != 3 and (i:=G[r+8]) != 3:
            ok = 1
            for dr, dc in N:
                if 4>dr>-1<r+dc<4 and (G[4*dr+r+dc], i) in X: ok = 0; break
            if ok: z.append(b+L*((3-i)<<(2*r)))
        if (i:=G[r+4]) != 3 and G[r+8] != 3 and G[r+12] == 3:
            ok = 1
            for dr, dc in N:
                if 4>3+dr>-1<r+dc<4 and (G[4*(3+dr)+r+dc], i) in X: ok = 0; break
            if ok: z.append(b-L*((3-i)<<(2*r+8)))
        if G[r+4] == 3 and G[r+8] != 3 and (i:=G[r+12]) != 3:
            ok = 1
            for dr, dc in N:
                if 4>1+dr>-1<r+dc<4 and (G[4*(1+dr)+r+dc], i) in X: ok = 0; break
            if ok: z.append(b+L*((3-i)<<(2*r+8)))
    return z
s = int(''.join(map(str, M[::-1])), 4)
D = {s:0}; Q = [s]
for u in Q:
    for v in f(u):
        if v not in D:
            D[v] = D[u]+1
            if v%4 == 0: print(D[v]); exit()
            Q.append(v)