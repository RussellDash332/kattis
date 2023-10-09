from math import *
import sys
for l in sys.stdin:
    a = sorted(map(int, l.split()[1:]))[::-1]; d = [1]*len(a); m = 0
    for i in range(len(a)):
        if d[i]==0: continue
        for j in range(len(a)):
            if i != j and gcd(a[i], a[j]) > 1: d[i] = d[j] = 0; break
        if d[i]: print(a[i]); break