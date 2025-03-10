from math import *
N = int(input()); Z = 0
P = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    H = {}
    for j in range(N):
        if j == i: continue
        d = gcd(dx:=P[j][0]-P[i][0], dy:=P[j][1]-P[i][1]); dx //= d; dy //= d
        if dx < 0: dx, dy = -dx, -dy
        if (f:=(dx, dy)) not in H: H[f] = 0
        H[f] += 1
    for a, b in H:
        if (-b, a) in H: Z += H[(a, b)]*H[(-b, a)]
print(Z)