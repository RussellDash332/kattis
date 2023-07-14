# sauce: https://codeforces.com/blog/entry/18051
def apply(p, v, k):
    t[p] = v*k
    if p < N: d[p] = v
def push(l):
    s = B; k = 1<<(s-1); l += N
    while s > 0:
        i = l>>s
        if d[i]: apply(2*i, d[i], k), apply(2*i+1, d[i], k); d[i] = 0
        s -= 1; k //= 2
def modify(l, r, v):
    push(l), push(r-1)
    cl = cr = 0; k = 1
    l += N; r += N
    while l < r:
        if cl: t[l-1] = d[l-1]*k if d[l-1] else t[2*l-2] + t[2*l-1]
        if cr: t[r] = d[r]*k if d[r] else t[2*r] + t[2*r+1]
        if l%2: apply(l, v, k); l += 1; cl = 1
        if r%2: r -= 1; apply(r, v, k); cr = 1
        l //= 2; r //= 2; k *= 2
    l -= 1
    while r > 0:
        if cl: t[l] = d[l]*k if d[l] else t[2*l] + t[2*l+1]
        if cr and (not cl or l != r): t[r] = d[r]*k if d[r] else t[2*r] + t[2*r+1]
        l //= 2; r //= 2; k *= 2

import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, Q = map(int, input().split())
ops, ints = [], {0, N}
for _ in range(Q):
    c, *se = map(int, input().split())
    if c == 1: s, e = se; ops.append((1, s-1, e)), ints.add(s-1), ints.add(e)
    else: ops.append((2, None, None))
ans = []
ints = sorted(ints)
rev = {e:i for i,e in enumerate(ints)}
M, N = N+len(rev)-1, len(rev)-1
B = len(bin(N))-2
t, d = [0]*2*N, [0]*N
for i in range(N): modify(i, i+1, ints[i+1]-ints[i]+1)
for c, s, e in ops: modify(rev[s], rev[e], 1) if c == 1 else ans.append(M-t[1])
if ans: sys.stdout.write('\n'.join(map(str, ans)))