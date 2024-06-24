import sys; input = sys.stdin.readline; from collections import *
while True:
    try: X, Y, Z, N = map(int, input().split()); R = {}; A = {}
    except: break
    for _ in range(N):
        x, y, z = map(int, input().split())
        if x not in R: R[x] = {}
        if y not in R[x]: R[x][y] = []
        R[x][y].append(z); A[(x, y, z)] = len(A)
    print('YES'); sx = 1; mx = max(R); C = [None]*N
    for x in sorted(R):
        ex = x if x != mx else X; sy = 1; my = max(R[x])
        for y in sorted(R[x]):
            ey = y if y != my else Y; sz = 1; mz = max(R[x][y])
            for z in sorted(R[x][y]): C[A[(x, y, z)]] = (sx, sy, sz, ex, ey, z if z != mz else Z); sz = z+1
            sy = y+1
        sx = x+1
    for c in C: print(*c)