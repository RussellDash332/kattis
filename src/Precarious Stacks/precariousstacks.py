import sys; input = sys.stdin.readline
class Node:
    def __init__(s, l, r):
        s.l = l; s.r = r; s.lc = s.rc = None; s.s = s.z = 0
    def push(s):
        if s.l == s.r: return
        if not s.lc: s.lc = Node(s.l, mi:=(s.l+s.r)//2); s.rc = Node(mi+1, s.r)
        s.lc.s = max(s.lc.s, s.z); s.lc.z = max(s.lc.z, s.z); s.rc.s = max(s.rc.s, s.z); s.rc.z = max(s.rc.z, s.z); s.z = 0
    def paint(s, lq, rq, v):
        if s.l > rq or s.r < lq: return
        if s.l >= lq and s.r <= rq: s.s = s.z = v; return
        s.push(); s.lc.paint(lq, rq, v); s.rc.paint(lq, rq, v); s.s = max(s.lc.s, s.rc.s)
    def get(s, lq, rq):
        if s.l > rq or s.r < lq: return 0
        if s.l >= lq and s.r <= rq: return s.s
        s.push(); return max(s.lc.get(lq, rq), s.rc.get(lq, rq))
T = Node(0, M:=2*10**9+9)
for _ in range(int(input())): x, s = map(int, input().split()); T.paint(x, x+s-1, T.get(x, x+s-1)+s); print(T.get(0, M))