import sys
from math import log10
for l in sys.stdin:
    t, a, b = map(int, l.split())
    k = f'({t}^{a}-1)/({t}^{b}-1)'
    if a % b or (a-b)*log10(t) > 101: print(k, 'is not an integer with less than 100 digits.'); continue
    if a == b and t > 1: print(k, 1); continue
    aa, bb = t**a-1, t**b-1
    if bb == 0 or aa % bb: print(k, 'is not an integer with less than 100 digits.')
    elif (q:=aa//bb) < 10**99: print(k, q)
    else: print(k, 'is not an integer with less than 100 digits.')