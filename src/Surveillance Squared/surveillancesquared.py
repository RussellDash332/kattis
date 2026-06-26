import sys; input = sys.stdin.readline
from math import *
while 1:
    try: n = int(input())
    except: break
    P = []; V = []
    for _ in range(n):
        x, y, a, b = map(int, input().split())
        P.append((x, y)); V.append((a, b))
    for i in range(n):
        x, y = P[i]; a, b = V[i]; t = atan2(b, a); z = 0
        for j in range(n):
            if i == j: continue
            x2, y2 = P[j]
            u = atan2(y2-y, x2-x)
            if (t-pi/4)%(2*pi)-1e-9 <= u%(2*pi) <= (t+pi/4)%(2*pi)+1e-9 or (t+pi/4)%(2*pi)-1e-9 <= (u+pi/2)%(2*pi) <= (t+3*pi/4)%(2*pi)+1e-9: z += 1
        print(z)
    print()