import sys; input = sys.stdin.readline
from math import *
N = int(input())
g = [{} for _ in range(N)]
for _ in range(N-1): a, b, x, t = map(int, input().split()); g[a-1][b-1] = (x/100, t)
l = [*map(lambda x: log(float(x)) if float(x) != -1 else None, input().split())]

def propagate(k):
    stack = [(k, 0)]
    while stack:
        liq, u = stack.pop()
        if not g[u]: # is a leaf
            if l[u] != None and liq < l[u]: return False
        for v, (p, t) in g[u].items():
            f = liq + log(p)
            if t and f > 0: stack.append((2*f, v)) # use log avoids FPE
            else: stack.append((f, v))
    return True

prec = 10**14
lo, hi = 0, int(log(2*10**9+1)*prec+prec)
while abs(lo-hi) > 1:
    mid = (lo+hi)//2
    if propagate(mid/prec): hi = mid
    else: lo = mid
print(exp(mid/prec))