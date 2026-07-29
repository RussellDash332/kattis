from math import *
n = int(input())
P = [[*map(int, input().split())] for _ in range(n)]
Z = 0
for i in range(n):
    x1, y1 = P[i]; H = {}
    for j in range(n):
        if i != j:
            x2, y2 = P[j]
            dx, dy = x2-x1, y2-y1
            d = gcd(dx, dy)
            dx //= d; dy //= d
            k = (dx, dy)
            if k not in H: H[k] = 0
            H[k] += 1
    for dx, dy in H:
        k = H[(dx, dy)]
        if (-dy, dx) in H: Z += H[(-dy, dx)]*k
        if (dy, -dx) in H: Z += H[(dy, -dx)]*k
print(Z//2)