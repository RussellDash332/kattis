from math import *

def ts(sx, sy, vx, vy, x, y): # pmo :(
    def f(u): return (sx+u*vx-x)**2+(sy+u*vy-y)**2
    a, b = 0, min(1, (69-sx)/vx if vx > 0 else (1-sx)/vx if vx < 0 else 1e9, (139.5-sy)/vy if vy > 0 else (1-sy)/vy if vy < 0 else 1e9); gr = (5**0.5-1)/2; tol = 1e-8
    if b == 1e9: return 0
    while b-a>tol:
        if f(μ:=(1-gr)*a+gr*b) > f(λ:=gr*a+(1-gr)*b): b = μ
        else: a = λ
    t = (a+b)/2
    if f(t) <= 4+1e-9: return t
    else: return 0

n = int(input()); S = []
for _ in range(n):
    c, x, y = input().split(); x = float(x); y = float(y)
    if c != 'white': S.append((c, x, y))
    else: sx, sy = x, y
on = input(); vx, vy = map(float, input().split()); a = atan2(vy, vx); v = hypot(vx, vy)

while v > 1e-9:
    T = []; h = min((69-sx)/vx if vx > 0 else (1-sx)/vx if vx < 0 else 1e9, (139.5-sy)/vy if vy > 0 else (1-sy)/vy if vy < 0 else 1e9)
    for c, x, y in S:
        t = ts(sx, sy, vx, vy, x, y)
        if t: T.append((t, c))
    if T: print('FHOIUTL'[min(T)[1]==on::2]); exit()
    sx += vx*h; sy += vy*h; vx *= 1-h; vy *= 1-h; v *= 1-h
    if sx == 1 or sx == 69: vx = -vx
    if sy == 1 or sy == 139.5: vy = -vy
print('MISS')