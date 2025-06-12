def madd(x, y):
    return (x[0]+y[0])%M, (x[1]+y[1])%M, (x[2]+y[2])%M, (x[3]+y[3])%M

def mmul(x, y):
    return (x[0]*y[0]+x[1]*y[2])%M, (x[0]*y[1]+x[1]*y[3])%M, (x[2]*y[0]+x[3]*y[2])%M, (x[2]*y[1]+x[3]*y[3])%M

def mpow(x, n):
    if n == 0: return 1, 0, 0, 1
    if n%2: return mmul(x, mpow(x, n-1))
    return mmul(t:=mpow(x, n//2), t)

class Node:
    def __init__(s, l, r):
        s.l = l; s.r = r; s.lc = s.rc = None; s.s = s.z = 1, 0, 0, 1
    def push(s):
        if s.l == s.r: return
        mi = (s.l+s.r)//2
        if not s.lc: s.lc = Node(s.l, mi); s.rc = Node(mi+1, s.r)
        s.lc.s = mmul(s.lc.s, s.z); s.lc.z = mmul(s.lc.z, s.z); s.rc.s = mmul(s.rc.s, s.z); s.rc.z = mmul(s.rc.z, s.z); s.z = 1, 0, 0, 1
    def add(s, lq, rq, v):
        if s.l > rq or s.r < lq: return
        if s.l >= lq and s.r <= rq: s.s = mmul(s.s, v); s.z = mmul(s.z, v); return
        s.push(); s.lc.add(lq, rq, v); s.rc.add(lq, rq, v); s.s = madd(s.lc.s, s.rc.s)
    def get(s, lq, rq):
        if s.l > rq or s.r < lq: return 0, 0, 0, 0
        if s.l >= lq and s.r <= rq: return s.s
        s.push(); return madd(s.lc.get(lq, rq), s.rc.get(lq, rq))

import sys; input = sys.stdin.readline
n, q = map(int, input().split()); T = Node(1, n); a = [*map(int, input().split())]; M = 10**9+7
for i in range(n): T.add(i+1, i+1, mpow((1, 1, 1, 0), a[i]))
for _ in range(q):
    c, *x = map(int, input().split())
    if c%2: l, r, v = x; T.add(l, r, mpow((1, 1, 1, 0), v))
    else: print(T.get(*x)[1])