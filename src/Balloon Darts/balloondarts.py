from random import *
N = int(input())
P = [[*map(int, input().split())] for _ in range(N)]
def f(P, k):
    if len(P) <= 2*k: return 0
    if P and k < 1: return 1
    p = sample(P, k+1)
    for i in range(k+1):
        xi, yi = p[i]
        for j in range(i):
            dy = yi-p[j][1]; dx = xi-p[j][0]; C = yi*dx-xi*dy
            if not f([(x, y) for x, y in P if dy*x-dx*y+C != 0], k-1): return 0
    return 1
print('im'*f(P, 3)+'possible')