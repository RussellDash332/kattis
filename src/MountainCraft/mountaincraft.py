L = []; R = []; LC = []; RC = []; S = []; Z = []; M = []; C = []
def create(l, r):
    L.append(l); R.append(r); LC.append(-1); RC.append(-1); S.append(0); Z.append(0); M.append(0); C.append(r-l+1)
    return len(L)-1
def push(i):
    l = L[i]; r = R[i]
    if l == r: return
    mi = (l+r)>>1
    if LC[i] < 0: LC[i] = create(l, mi); RC[i] = create(mi+1, r)
    lc = LC[i]; rc = RC[i]; z = Z[i]
    if z>0: S[lc] += C[lc]*(M[lc]<1); S[rc] += C[rc]*(M[rc]<1)
    elif z<0: S[lc] -= C[lc]*(M[lc]==-z); S[rc] -= C[rc]*(M[rc]==-z)
    M[lc] += z; M[rc] += z; Z[lc] += z; Z[rc] += z; Z[i] = 0
def update(lq, rq, v, i=0):
    stk = [(i, 0)]
    while stk:
        i, b = stk.pop()
        if b>0:
            S[i] = S[lc:=LC[i]]+S[rc:=RC[i]]
            M[i] = min(M[lc], M[rc])
            C[i] = C[lc]*(M[lc]==M[i])+C[rc]*(M[rc]==M[i])
        else:
            l = L[i]; r = R[i]
            if l > rq or r < lq: continue
            if l >= lq and r <= rq:
                if v>0: S[i] += C[i]*(M[i]<1); M[i] += 1; Z[i] += 1
                else: S[i] -= C[i]*(M[i]==1); M[i] -= 1; Z[i] -= 1
                continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
def get(lq, rq, i=0):
    stk = [(i, 0)]; tmp = []
    while stk:
        i, b = stk.pop()
        if b>0: tmp.append(tmp.pop()+tmp.pop())
        else:
            l = L[i]; r = R[i]
            if l > rq or r < lq: tmp.append(0); continue
            if l >= lq and r <= rq: tmp.append(S[i]); continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
    return tmp[0]
N, W = map(int, input().split())
V = set(); T = create(0, W); D = 2**.5
for _ in range(N):
    x, y = map(int, input().split())
    if (x, y) in V: v = -1; V.discard((x, y))
    else: v = 1; V.add((x, y))
    update(max(x-y, 0), min(x+y, W)-1, v); print(get(0, W)*D)