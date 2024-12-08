def pf(n, K):
    for p in map(int, subprocess.check_output(f"factor {n}|cut -d':' -f2",shell=True).split()): E[p] += K

import os, io, subprocess; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from math import gcd; from random import *; from array import *; from collections import *; U = 24000; MOD = 10**9+7; Z = 1; P, N, M = map(int, input().split()); E = Counter(); K = array('i', [pow(d, P, MOD) for d in range(U+1)]); C = array('i', [(K[d+1]-2*K[d]+K[d-1])%MOD for d in range(1, U)])
for i in map(int, input().split()): pf(i, -1)
for i in map(int, input().split()): pf(i, 1)
for i in E:
    if E[i] < 0: print(0), exit(0)
    elif E[i] > 0: Z *= C[E[i]-1]; Z %= MOD
print(Z)