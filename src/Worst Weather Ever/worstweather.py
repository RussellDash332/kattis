# https://stackoverflow.com/questions/31106459/how-to-adapt-fenwick-tree-to-answer-range-minimum-queries/34602284#34602284
def update(a, i, x):
    a[i] = x
    while i > 1:
        i //= 2; a[i] = a[2*i]
        if a[2*i+1] > a[2*i]: a[i] = a[2*i+1]
def rmq(a, i, j):
    x = -INF
    while i < j:
        if i%2 == 0: i //= 2
        else:
            if a[i] > x: x = a[i]
            i = i//2+1
        if j%2 == 0: j //= 2
        else:
            if a[j-1] > x: x = a[j-1]
            j //= 2
    return x

import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; print = sys.stdout.write; from bisect import *; INF = 10**9+1
while (n:=int(input())):
    R = {}
    for _ in range(n): y, r = map(int, input().split()); R[y] = r
    A = sorted(R); F = [0]*2*n
    for i in range(n): update(F, i+n, R[A[i]])
    for _ in range(int(input())):
        y, x = map(int, input().split()); nxt = bisect_left(A, y+1); prv = bisect_left(A, x)-1
        if x not in R:
            if y in R and rmq(F, nxt+n, prv+n+1) >= R[y]: print('false\n')
            else: print('maybe\n')
        elif rmq(F, nxt+n, prv+n+1) >= R[x]: print('false\n')
        elif y in R:
            if R[y] < R[x]: print('false\n')
            elif prv-nxt == x-y-2: print('true\n')
            else: print('maybe\n')
        else: print('maybe\n')
    input(); print('\n')