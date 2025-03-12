import sys; input = sys.stdin.readline; from bisect import *
h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else(min(a[0],b[0]),max(a[1],b[1]))
def merge(ints):
    r = []
    for j in ints:
        if r and (k:=h(r[-1], j)): r[-1] = k
        else: r.append(j)
    return r
n, r = map(int, input().split()); p = int(r**.25)
D = [[] for _ in range(10**5+20)]; Z = 0
def cover(x, y):
    for yy in range(y-p, y+p+1): s = int((r-(yy-y)**4)**.5); insort(D[yy], (x-s, x+s)); D[yy] = merge(D[yy])
cover(x:=0, y:=0)
for s in input().strip():
    if s == 'L': x -= 1
    elif s == 'R': x += 1
    elif s == 'U': y += 1
    else: y -= 1
    cover(x, y)
for t in D:
    for s, e in t: Z += e-s+1
print(Z)