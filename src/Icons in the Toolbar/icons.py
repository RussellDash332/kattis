import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
n = int(input()); s = array('i', [int(input()) for _ in range(2*n)]); p = [0]; q = [0]; t = 1
for i in s:
    if len(p) <= n: p.append(p[-1]+i)
    if t: q.append(q[-1]+i)
    t ^= 1
print(min((p[k]+q[n]-q[k])*(s[0]+s[k]) for k in range(1, n+1)))