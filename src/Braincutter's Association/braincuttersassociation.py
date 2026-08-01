L = []; R = []; LC = []; RC = []; S = []; Z = []
INIT = (10**9, 0)
def combine(a, b):
    ma, Ma = a; mb, Mb = b; return min(ma, mb), max(Ma, Mb)
def create(l, r):
    L.append(l); R.append(r); LC.append(-1); RC.append(-1); S.append(INIT); Z.append(INIT); return len(L)-1
def push(i):
    l = L[i]; r = R[i]
    if l == r: return
    mi = (l+r)>>1
    if LC[i] < 0: LC[i] = create(l, mi); RC[i] = create(mi+1, r)
    lc = LC[i]; rc = RC[i]; z = Z[i]; S[lc] = combine(S[lc], z); S[rc] = combine(S[rc], z); Z[lc] = combine(Z[lc], z); Z[rc] = combine(Z[rc], z); Z[i] = INIT
def update(lq, rq, v, i=0):
    stk = [(i, 0)]
    while stk:
        i, b = stk.pop()
        if b>0: S[i] = combine(S[LC[i]], S[RC[i]])
        else:
            l = L[i]; r = R[i]
            if l > rq or r < lq: continue
            if l >= lq and r <= rq: S[i] = v; Z[i] = v; continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
def get(lq, rq, i=0):
    stk = [(i, 0)]; tmp = []
    while stk:
        i, b = stk.pop()
        if b>0: tmp.append(combine(tmp.pop(), tmp.pop()))
        else:
            l = L[i]; r = R[i]
            if l > rq or r < lq: tmp.append(INIT); continue
            if l >= lq and r <= rq: tmp.append(S[i]); continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
    return tmp[0]

import sys; input = sys.stdin.readline
C = create(0, 10**9); D = create(0, 10**9); H = {}
for _ in range(int(input())):
    t, c, d = map(int, input().split())
    if t<2:
        update(c, c, (d, d), C); update(d, d, (c, c), D)
        if (c, d) not in H: H[(c, d)] = 0
        H[(c, d)] += 1
    elif t<3:
        H[(c, d)] -= 1
        if H[(c, d)] < 1: update(c, c, INIT, C); update(d, d, INIT, D)
    else:
        l, h = get(c, d, (C, D)[t>3])
        if l>h: print('Enginn!')
        else: print(f'{l} {h}')