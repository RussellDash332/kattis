# 65 pts :)
import sys; input = sys.stdin.readline; from array import *
N = int(input())
A = array('I', map(int, input().split()))
F = array('I', [0]*-~N)
for i in range(N-1): A[i] -= 1
def f(x):
    if F[x]: return F[x]
    s = array('I', [1]*N); w = 0
    for u in range(N-1, -1, -1):
        if s[u] > x: w += 1
        else: s[A[u-1]] += s[u]
    F[x] = w; return w
Z = array('I', [0]*N); p = 1
while p < N:
    c = f(p); lo, hi = p, N
    while lo < hi:
        if f(mi:=(lo+hi)//2) != c: hi = mi
        else: lo = mi+1
    Z[c] = p; p = lo
for i in range(1, N):
    if Z[i] < 1: Z[i] = Z[i-1]
sys.stdout.write(' '.join(map(str, Z[1:])))