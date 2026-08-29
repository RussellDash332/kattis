L = []; R = []; LC = []; RC = []; S = []; Z = []

def combine(a, b):
    return min(a[0], b[0]), max(a[1], b[1])
def create(l, r):
    L.append(l); R.append(r); LC.append(-1); RC.append(-1); S.append((0, 0)); Z.append(0)
    return len(L)-1
def push(i):
    l = L[i]; r = R[i]
    if l == r: return
    mi = (l+r)>>1
    if LC[i] < 0: LC[i] = create(l, mi); RC[i] = create(mi+1, r)
    lc = LC[i]; rc = RC[i]; z = Z[i]
    S[lc] = (S[lc][0]+z, S[lc][1]+z); S[rc] = (S[rc][0]+z, S[rc][1]+z)
    Z[lc] += z; Z[rc] += z; Z[i] = 0
def update(lq, rq, v, i=0):
    stk = [(i, 0)]
    while stk:
        i, b = stk.pop()
        if b>0: S[i] = combine(S[LC[i]], S[RC[i]])
        else:
            l = L[i]; r = R[i]
            if l > rq or r < lq: continue
            if l >= lq and r <= rq:
                S[i] = (S[i][0]+v, S[i][1]+v)
                Z[i] += v
                continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
def get(lq, rq, i=0):
    stk = [(i, 0)]; tmp = []
    while stk:
        i, b = stk.pop()
        if b>0: tmp.append(combine(tmp.pop(), tmp.pop()))
        else:
            l = L[i]; r = R[i]
            if l > rq or r < lq: tmp.append((10**9, -10**9)); continue
            if l >= lq and r <= rq: tmp.append(S[i]); continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
    return tmp[0]

import sys; input = sys.stdin.readline
C, N, O = map(int, input().split()); create(0, C-1)
for _ in range(O):
    c, *v = input().split()
    if c == 'state': x = int(v[0]); print(get(x, x)[0])
    elif c == 'change':
        x, v = map(int, v)
        k = get(x, x)[0]; d = max(min(k+v, N), 0)-k
        update(x, x, d); print(d)
    else:
        a, b, v = map(int, v)
        mi, ma = get(a, b)
        d = min(max(min(mi+v, N), 0)-mi, max(min(ma+v, N), 0)-ma, key=abs)
        update(a, b, d); print(d)