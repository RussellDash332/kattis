from bisect import *
def p(a): r = {e:i for i,e in enumerate(a)}; return [r[i] for i in range(len(a))]
def lis(A):
    B = []
    for e in A:
        p = bisect(B, e-1)
        if p == len(B): B.append(e)
        else: B[p] = e
    return len(B)
n, m, *s = open(0)
m = p(p([*map(lambda x: int(x)-1, m.split())]))
for r in s: print(lis([m[i] for i in p([*map(lambda x: int(x)-1, r.split())])]))