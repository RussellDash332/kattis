import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from collections import *; from array import *; from bisect import *
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    z = array('i', [-1]*n); s = []
    for i in range(n-1, -1, -1):
        b = bisect(s, [x:=a[i], 10**9])
        if b == len(s):
            if s and s[-1][0]<=x<s[-1][1]: x = s[-1][1]
            if s and s[-1][1] == x: s[-1][1] += 1
            else: s.append([x, x+1])
        else:
            if b and s[b-1][0]<=x<s[b-1][1]: x = s[b-1][1]
            if x+1 == s[b][0]:
                s[b][0] -= 1
                if b and s[b-1][1] == s[b][0]: s[b-1][1] = s[b][1]; s.pop(b)
            elif b and x == s[b-1][1]:
                s[b-1][1] += 1
                if b and s[b-1][1] == s[b][0]: s[b-1][1] = s[b][1]; s.pop(b)
            else: s.insert(b, [x, x+1])
        z[i] = x
    lo, hi = 0, max(z[i]-a[i] for i in range(n))
    while lo<hi:
        mi = (lo+hi)//2
        if max(Counter(min(a[i]+mi, z[i]) for i in range(n)).values())>k: lo = mi+1
        else: hi = mi
    sys.stdout.write(str(lo)+'\n')