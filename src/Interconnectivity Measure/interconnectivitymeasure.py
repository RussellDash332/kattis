import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
n, m = map(int, input().split()); K = len(bin(m))-2; p = array('i', range(n)); ra = array('b', [0]*n)
A = array('i', [0]*(1<<K)); B = array('i', [0]*(1<<K)); qA = array('i'); qB = array('i')
for i in range(1, m+1): a, b = map(int, input().split()); A[i] = a-1; B[i] = b-1
q = int(input()); Z = array('i', [-1]*q)
for i in range(q): a, b = map(int, input().split()); qA.append(a-1); qB.append(b-1)
def rs(i):
    p[i] = i; ra[i] = 0
def fi(i):
    if p[i] == i: return i
    p[i] = fi(p[i]); return p[i]
def un(i, j):
    if (x:=fi(i)) != (y:=fi(j)):
        if ra[x] > ra[y]: p[y] = x
        else: p[x] = y; ra[y] += ra[x] == ra[y]
def f(l, r, qu):
    if l+1 == r:
        for i in qu: Z[i] = l
        return
    for i in qu: rs(qA[i]); rs(qB[i])
    w = x = (l+r-1)>>1
    while x: rs(A[x]); rs(B[x]); x = (x-1)&w
    x = w; L = []; R = []
    while x: un(A[x], B[x]); x = (x-1)&w
    while qu:
        if fi(qA[i:=qu.pop()]) == fi(qB[i]): L.append(i)
        else: R.append(i)
    if L: f(l, w+1, L)
    if R: f(w+1, r, R)
f(0, 1<<K, [*range(q)])
for i in Z: sys.stdout.write(str(i)); sys.stdout.write('\n')