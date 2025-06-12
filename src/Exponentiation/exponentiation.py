from bisect import *
n, q = map(int, input().split()); d = [[]]; m = [0]*n; g = [0]; h = [0]
def cmp(x, y):
    for i in range(min(len(x), len(y))):
        if (v:=f(x[i], y[i])) != 1: return v-1
    return (len(x)>len(y))-(len(x)<len(y))
def f(x, y): return x==y or (g.index(x)<g.index(y))+(h.index(x)<h.index(y))
for _ in range(q):
    c, a, b = input().split(); a = int(a)-1; b = int(b)-1
    if c == '!': v = len(d); d.append([*d[m[a]]]); m[a] = v; insort(d[-1], m[b], key=g.index); insort_left(g, v, key=lambda x: cmp(d[v], d[x])); insort(h, v, key=lambda x: cmp(d[v], d[x]))
    else: print('<=>'[f(m[a], m[b])])