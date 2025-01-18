import sys; input = sys.stdin.readline
from bisect import *
n, m = map(int, input().split())
s = input().strip()
x, y = map(int, input().split())
X = x+y; Y = x-y
hx = {X:[Y]}; hy = {Y:[X]}
for _ in range(n-1):
    x, y = map(int, input().split())
    a = x+y; b = x-y
    if a%2-X%2 or b%2-Y%2: continue
    if a not in hx: hx[a] = []
    hx[a].append(b)
    if b not in hy: hy[b] = []
    hy[b].append(a)
for i in hx: hx[i].sort()
for i in hy: hy[i].sort()
for i in s:
    p = bisect_left(hy[Y], X)
    q = bisect_left(hx[X], Y)
    if i == 'A':
        if p < len(hy[Y])-1: o = hy[Y][p+1]; hx[X].pop(q); hy[Y].pop(p); X = o
    elif i == 'B':
        if q < len(hx[X])-1: o = hx[X][q+1]; hx[X].pop(q); hy[Y].pop(p); Y = o
    elif i == 'C':
        if q: o = hx[X][q-1]; hx[X].pop(q); hy[Y].pop(p); Y = o
    else:
        if p: o = hy[Y][p-1]; hx[X].pop(q); hy[Y].pop(p); X = o
print((X+Y)//2, (X-Y)//2)