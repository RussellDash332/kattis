import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
s, p, m, n = map(int, input().split()); t = array('i', map(int, input().split())); dp = [0]*(n+1)
for i in range(n-1, -1, -1):
    dp[i] = dp[i+1]+s; lo = 0; hi = n; x = t[i]+m
    while lo < hi:
        mi = (lo+hi)//2
        if t[mi] < x: lo = mi+1
        else: hi = mi
    if (v:=dp[lo]+p) < dp[i]: dp[i] = v
print(dp[0])