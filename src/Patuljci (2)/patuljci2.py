from array import *; from random import *; from bisect import *; import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, c = map(int, input().split()); A = array('i', [*map(int, input().split())]); B = sorted(n*A[i]+i for i in range(n))
for _ in range(int(input())):
    a, b = map(int, input().split()); a -= 1; b -= 1; ok = 0
    for _ in range(15):
        x = A[randint(a, b)]
        if 2*(bisect_left(B, n*x+b+1)-bisect_left(B, n*x+a)) > b-a+1: ok = 1; break
    if ok: print('yes', x)
    else: print('no')