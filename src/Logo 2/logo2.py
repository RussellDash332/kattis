import sys; input = sys.stdin.readline
from math import *
EPS = 1e-6
for _ in range(int(input())):
    CA = []
    for _ in range(int(input())):
        c, a = input().strip().split()
        CA.append((c, a))
        if a == '?': tr_or_rt = c in ['fd', 'bk']
    if tr_or_rt:
        A = pi; X = Y = 0
        for c, a in CA:
            if a == '?':    MC, MA = c, A
            elif c == 'fd': X += int(a)*cos(A); Y += int(a)*sin(A)
            elif c == 'bk': X -= int(a)*cos(A); Y -= int(a)*sin(A)
            elif c == 'lt': A += int(a)*pi/180
            else:           A -= int(a)*pi/180
        print((1-2*(MC=='fd'))*round(X/cos(MA)))
    else:
        for aa in range(360):
            A = pi; X = Y = 0
            for c, a in CA:
                if a == '?':    a = aa
                if c == 'fd':   X += int(a)*cos(A); Y += int(a)*sin(A)
                elif c == 'bk': X -= int(a)*cos(A); Y -= int(a)*sin(A)
                elif c == 'lt': A += int(a)*pi/180
                else:           A -= int(a)*pi/180
            if abs(X) < EPS and abs(Y) < EPS: print(aa); break