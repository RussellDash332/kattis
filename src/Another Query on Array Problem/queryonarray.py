from array import *
L = 10**5; M = 10**9+7; H = pow(2, -1, M); S = pow(3, -1, M)
A = array('i', ((i*i+i)*H%M for i in range(L))); A.append(0)
B  = array('i', (A[i]*(2*i+1)*S%M for i in range(L))); B.append(0)
C = array('i', (A[i]**2%M for i in range(L))); C.append(0)

def make(lm1, r, v):
    return (v[0]*(r-lm1)%M, v[1]*(A[r]-A[lm1])%M, v[2]*(B[r]-B[lm1])%M, v[3]*(C[r]-C[lm1])%M)

def vadd(v1, v2):
    v1[0] = (v1[0]+v2[0])%M; v1[1] = (v1[1]+v2[1])%M; v1[2] = (v1[2]+v2[2])%M; v1[3] = (v1[3]+v2[3])%M

class Node:
    def __init__(s, l, r):
        s.l = l; s.r = r; s.lc = s.rc = None; s.s = [0]*4; s.z = [0]*4
    def push(s):
        if s.l == s.r: return
        mi = (s.l+s.r)//2
        if not s.lc: s.lc = Node(s.l, mi); s.rc = Node(mi+1, s.r)
        vadd(s.lc.s, make(s.l-1, mi, s.z)); vadd(s.lc.z, s.z)
        vadd(s.rc.s, make(mi, s.r, s.z)); vadd(s.rc.z, s.z)
        s.z[0] = s.z[1] = s.z[2] = s.z[3] = 0
    def add(s, lq, rq, v):
        if s.l > rq or s.r < lq: return
        if s.l >= lq and s.r <= rq: vadd(s.s, make(s.l-1, s.r, v)); vadd(s.z, v); return
        s.push(); s.lc.add(lq, rq, v); s.rc.add(lq, rq, v)
        s.s[0] = s.s[1] = s.s[2] = s.s[3] = 0
        vadd(s.s, s.lc.s); vadd(s.s, s.rc.s)
    def get(s, lq, rq, t):
        if s.l > rq or s.r < lq: return
        if s.l >= lq and s.r <= rq: return vadd(t, s.s)
        s.push(); s.lc.get(lq, rq, t); s.rc.get(lq, rq, t)

import sys; input = sys.stdin.readline
N, Q = map(int, input().split()); T = Node(0, N-1); Z = []
for _ in range(Q):
    c, x, y = map(int, input().split()); x -= 1
    if c == 0: t = [0]*4; T.get(x, y-1, t); Z.append((t[0]+t[1]+t[2]+t[3])%M)
    else: s = 3-2*c; u = 2-x; T.add(x, y-1, (s*(u*u*u-u), s*(3*u*u-1), s*3*u, s))
sys.stdout.write('\n'.join(map(str, Z)))