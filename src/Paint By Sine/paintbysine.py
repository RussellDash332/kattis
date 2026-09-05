from math import *
for _ in range(int(input())):
    a, b, c, d, L, R = map(float, input().split()); V = {L, R}
    def f(x, u):
        while x < L: x += u
        while x > R: x -= u
        v = x
        while L <= v <= R: V.add(v); v += u
        v = x
        while L <= v <= R: V.add(v); v -= u
    if a-c: f((d-b)/(a-c), abs(2*pi/(a-c)))
    if a+c: f((pi-b-d)/(a+c), abs(2*pi/(a+c)))
    V = sorted(V); D = B = Y = 0
    for i in range(len(V)-1):
        s = V[i]; e = V[i+1]; m = (s+e)/2; v = cos(a*e+b)/a-cos(a*s+b)/a; w = cos(c*s+d)/c-cos(c*e+d)/c
        if sin(a*m+b) > sin(c*m+d): B -= v+w; Y += w+e-s
        else: D += v+w; Y -= v-e+s
    print(2*(R-L)-Y-D-B, Y, D, B)