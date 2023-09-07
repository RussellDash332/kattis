from math import *
import sys; input = sys.stdin.readline
n = int(input()); a = [*map(int, input().split())]
def f(r): return sum(asin(i/2/r) for i in a) <= pi
PREC = 10**7
lo, hi = ceil(max(a)/2*PREC), 10**14*PREC
while abs(lo-hi)>2:
    mi = (lo+hi)//2
    if f(mi/PREC): hi = mi
    else: lo = mi
print(mi/PREC)