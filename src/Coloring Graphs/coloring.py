from random import *

def shuffled(r):
    r = [*r]; shuffle(r); return r

def assign():
    a = [-1]*c
    def bt(cc, x, r):
        a[cc] = x; r += 1
        for dd in g[cc]:
            if a[dd] == x: a[cc] = -1; r -= 1; return 0
        for dd in g[cc]:
            ok = 1
            if a[dd] == -1:
                ok2 = 0
                for y in range(12):
                    if x != y and bt(dd, y, r): ok2 = 1; break
                ok *= ok2
            if 1-ok: a[cc] = -1; r -= 1; return 0
        return 1
    for cc in shuffled(range(c)):
        if a[cc] == -1:
            if 1-bt(cc, 0, 0): return 0
    return max(a)+1

c = int(input()); g = []
for _ in range(c): g.append([*map(int, input().split())])
print(min(assign() for _ in range(20)))