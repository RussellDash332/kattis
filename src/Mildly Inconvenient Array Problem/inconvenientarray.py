# only for subtask 1 and 2
import sys; input = sys.stdin.readline
from array import *; print = sys.stdout.write
L = array('I'); R = array('I'); LC = array('i'); RC = array('i'); S = []; Z = array('l')
Z0 = (0, 0, 0, 0)
def combine(a, b):
    sa, pa, qa, ma = a
    sb, pb, qb, mb = b
    return (sa+sb, max(pa, sa+pb), max(qb, sb+qa), max(ma, mb, qa+pb))
def create(l, r):
    L.append(l); R.append(r); LC.append(-1); RC.append(-1); S.append(Z0); Z.append(0)
    return len(L)-1
def push(i):
    l = L[i]; r = R[i]
    if l == r: return
    mi = (l+r)>>1
    if LC[i] < 0: LC[i] = create(l, mi); RC[i] = create(mi+1, r)
    lc = LC[i]; rc = RC[i]; z = Z[i]
    e, f, g, h = S[lc]
    S[lc] = (e+z, f+z, g+z, h+z)
    e, f, g, h = S[rc]
    S[rc] = (e+z, f+z, g+z, h+z)
    Z[lc] += z
    Z[rc] += z
    Z[i] = 0
def pu(lq, v, i=0):
    stk = [2*i]
    while stk:
        i, b = divmod(stk.pop(), 2)
        if b: S[i] = combine(S[LC[i]], S[RC[i]])
        else:
            l = L[i]; r = R[i]
            if l > lq or r < lq: continue
            if l >= lq >= r:
                e, f, g, h = S[i]
                S[i] = (e+v, f+v, g+v, h+v)
                Z[i] += v
                continue
            push(i); stk.append(2*i+1); stk.append(2*LC[i]); stk.append(2*RC[i])
def get(lq, rq, i=0):
    stk = [2*i]; tmp = []
    while stk:
        i, b = divmod(stk.pop(), 2)
        if b: tmp.append(combine(tmp.pop(), tmp.pop()))
        else:
            l = L[i]; r = R[i]
            if l > rq or r < lq: tmp.append(Z0); continue
            if l >= lq and r <= rq: tmp.append(S[i]); continue
            push(i); stk.append(2*i+1); stk.append(2*LC[i]); stk.append(2*RC[i])
    return tmp[0][3]
N, Q = map(int, input().split())
A = array('l', map(int, input().split()))
if N*Q <= 5*10**8:
    for _ in range(Q):
        c, *v = input().split()
        if c == '+':
            l, r, x = map(int, v)
            for i in range(l-1, r): A[i] += x
        else:
            l, r = map(int, v); m = u = 0
            for i in range(l-1, r): m = max(m, u:=max(u+A[i], 0))
            print(str(m)+'\n')
    exit()
T = create(0, N+1)
for i in range(N): pu(i+1, A[i])
for _ in range(Q):
    c, *v = input().split()
    if c == '+':
        l, r, x = map(int, v)
        for i in range(l, r+1): pu(i, x)
    else: l, r = map(int, v); print(str(get(l, r))+'\n')