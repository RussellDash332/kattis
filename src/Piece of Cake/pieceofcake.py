import sys; input = sys.stdin.readline
from math import *
from array import *
n, k = map(int, input().split()); a = 0
p = [[*map(float, input().split())] for _ in range(n)]
mat = [array('d', [-1]*n) for _ in range(n)]; cc = array('d', [0]); ck = [0]
for i in range(n-k): cc.append(cc[-1]+log10(k+i-1)-log10(i+1))
for i in range(k): ck.append(ck[-1]+log10(n-i)-log10(i+1))
nck = ck[-1]
for i in range(n-k+1):
    for j in range(n): mat[j][(n-k+1-i+j)%n] = cc[i]
for i in range(n):
    for j in range(n):
        if mat[i][j] != -1: a += 10**(mat[i][j]-nck)*(p[i][0]*p[j][1]-p[i][1]*p[j][0])
print(abs(a)/2)