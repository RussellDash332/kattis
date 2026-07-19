import sys; input = sys.stdin.readline; from bisect import *
for _ in range(int(input())):
    n, m, h, s = map(int, input().split())
    A = [0, *map(int, input().split()), h]; B = [0, *map(int, input().split()), h]
    for _ in '..':
        p = q = 0; a, b, u, v = A, B, n, m; c = 1
        while p < u+1 and q < v+1 and c:
            c = 0
            while p < u+1 and a[p+1]-a[p]<=s: p += 1; c = 1
            while q < v+1 and b[q+1]<=a[p]: q += 1; c = 1
            p, q, a, b, u, v = q, p, b, a, v, u
        A, B, n, m = B, A, m, n
        if p > u or q > v: print('YES'); break
    else: print('NO')