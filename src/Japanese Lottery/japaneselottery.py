import sys; input = sys.stdin.readline
w, h, q = map(int, input().split())
class Node:
    def __init__(s, l, r, w):
        s.l = l; s.r = r; s.lc = s.rc = None; s.s = [*range(w)]
    def push(s):
        if s.l == s.r: return
        if not s.lc: s.lc = Node(s.l, mi:=(s.l+s.r)//2, w); s.rc = Node(mi+1, s.r, w)
    def add(s, p, v):
        if s.l > p or s.r < p: return
        if s.l >= p and s.r <= p: s.s[v[0]], s.s[v[1]] = s.s[v[1]], s.s[v[0]]; return
        s.push(); s.lc.add(p, v); s.rc.add(p, v); s.s = [s.rc.s[i] for i in s.lc.s]
    def get(s, lq, rq):
        if s.l > rq or s.r < lq: return 0
        if s.l >= lq and s.r <= rq: return s.s
        s.push(); rr = s.rc.get(lq, rq); return [rr[i] for i in s.lc.get(lq, rq)]
T = Node(0, h-1, w)
def find(p):
    s = set(); z = 0
    for i in range(w):
        if i not in s:
            c = i; z += 1
            while True:
                c = p[c]; s.add(c)
                if c == i: break
    return w-z
for _ in range(q): y, x1, x2 = map(int, input().split()); T.add(y-1, (x1-1, x2-1)); print(find(T.get(0, h-1)))