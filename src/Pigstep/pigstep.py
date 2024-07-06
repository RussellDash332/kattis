def get(l, r, interactive):
    global Z; Z[0] -= 1
    assert Z[0] >= 0, interactive
    if interactive == True: print('ASK', l, r); return map(lambda x: x=='yes', input().strip().split())
    else: S, A = interactive; return [l<=S<=r, l<=A<=r]

def solve(L, R, interactive=True):
    global Z; Z = [11]
    while True:
        if R-L > 3:
            q1, q2, q3 = (L+round(i*(R-L)/4) for i in range(1, 4)); v1, v2 = get(L, q2, interactive); w1, w2 = get(q1, q3, interactive)
            if 2*v1+w1 == 2*v2+w2:
                L, R = (q3+1, q2+1, L, q1)[2*v1+w1], (R, q3, q1-1, q2)[2*v1+w1]
                if L == R: return (L, L)
            else: ls, rs, la, ra = (q3+1, q2+1, L, q1)[2*v1+w1], (R, q3, q1-1, q2)[2*v1+w1], (q3+1, q2+1, L, q1)[2*v2+w2], (R, q3, q1-1, q2)[2*v2+w2]; break
        else:
            m = (L+R)//2; v1, v2 = get(L, m, interactive)
            if v1 and v2: R = m
            elif not v1 and not v2: L = m+1
            else: ls, rs = (L, m) if v1 else (m+1, R); la, ra = (L, m) if v2 else (m+1, R); break
            if L == R: return (L, L)
    while rs > ls or ra > la:
        ms = (ls+rs)//2; ma = (la+ra)//2
        if ms < ma:
            if rs-ls < 2: ms += 1
            v1, v2 = get(ms, ma, interactive)
            if v1: ls = ms
            else: rs = ms-1
            if v2: ra = ma
            else: la = ma+1
        else:
            if ra-la < 2: ma += 1
            v1, v2 = get(ma, ms, interactive)
            if v1: rs = ms
            else: ls = ms+1
            if v2: la = ma
            else: ra = ma-1
    return (ls, la)

print('GUESS', *solve(1, 500, True)), exit(0)
for s in range(1, 501):
    for a in range(1, 501):
        assert (u:=solve(1, 500, (s, a))) == (s, a), (u, s, a)
        print('done', s, a); print()