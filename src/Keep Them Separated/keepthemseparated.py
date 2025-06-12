import sys; input = sys.stdin.readline
class FenwickTree2D:
    def __init__(self, r, c):
        self.ft = [0]*(r+1)*(c+1); self.r = r; self.c = c
    def add(self, r, c, e):
        r += 1; c += 1
        while r <= self.r:
            cc = c
            while cc <= self.c: self.ft[r*(self.c+1)+cc] += e; cc += cc&(-cc)
            r += r&(-r)
    def get(self, r, c):
        s = 0
        while r > 0:
            cc = c
            while cc > 0: s += self.ft[r*(self.c+1)+cc]; cc -= cc&(-cc)
            r -= r&(-r)
        return s%M
F = FenwickTree2D(2501, 2501); M = 10**9+7; C = {}
for i in range(int(input())):
    c, *v = map(int, input().split())
    if c == 1:
        x1, y1, x2, y2 = v; x = pow(2, i+1, M)
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        F.add(x2//2, y2//2, x); F.add(x2//2, y1//2, -x); F.add(x1//2, y2//2, -x); F.add(x1//2, y1//2, x); C[i+1] = (x1//2, y1//2, x2//2, y2//2)
    elif c == 2: x1, y1, x2, y2 = C[v[0]]; x = -pow(2, v[0], M); F.add(x2, y2, x); F.add(x2, y1, -x); F.add(x1, y2, -x); F.add(x1, y1, x)
    else: x1, y1, x2, y2 = v; sys.stdout.write('NY'[F.get(x1//2, y1//2)==F.get(x2//2, y2//2)])