import sys; input = sys.stdin.readline; from math import *
K = (3, 5, 6, 9, 10, 12); h, w = map(int, input().split()); m = [[1<<'rgbw'.index(x) for x in input().strip()] for _ in range(h)]; g = gcd(w, h)
for i in range(w):
    for j in range(i):
        b = [0]*16*g
        for k in range(h): b[k%g*16+(m[k][i]|m[k][j])] = 1
        for p in range(g):
            q = (p+j-i)%g
            for r in K:
                if b[16*p+r]&b[16*q+15-r]: print('possible'); exit()
print('impossible')