import sys
from math import gcd

input()
m = lambda: {'x': 0, 'y': 0, 'c': 0}

for l in sys.stdin:
    if not l.strip(): print(); continue
    eq1, eq2 = l.strip(), input().strip()
    (l1, r1), (l2, r2) = eq1.split(' = '), eq2.split(' = ')
    tl1, tr1, tl2, tr2 = ['+'] + l1.split(), ['+'] + r1.split(), ['+'] + l2.split(), ['+'] + r2.split() 
    cl1, cr1, cl2, cr2 = m(), m(), m(), m()
    for (c, tt) in ((cl1, tl1), (cr1, tr1), (cl2, tl2), (cr2, tr2)):
        for i, t in enumerate(tt):
            if i % 2:
                if t[-1] in 'xy':   c[t[-1]] += (1 if tt[i-1] == '+' else -1) * int((t[:-1] or 1) if t[:-1] != '-' else -1)
                else:               c['c'] += (1 if tt[i-1] == '+' else -1) * int(t)
    a, b, c, d, e, f = cl1['x']-cr1['x'], cl1['y']-cr1['y'], cr1['c']-cl1['c'], cl2['x']-cr2['x'], cl2['y']-cr2['y'], cr2['c']-cl2['c']
    nx, dx, ny, dy = c*e-b*f, a*e-b*d, c*d-a*f, b*d-a*e
    gx, gy = gcd(nx, dx),  gcd(ny, dy)
    if gx:
        nx //= gx
        dx //= gx
    if ny:
        ny //= gy
        dy //= gy
    if dx < 0: nx, dx = -nx, -dx
    if dy < 0: ny, dy = -ny, -dy
    if dx == 0: x = "don't know"
    elif nx % dx == 0: x = str(nx//dx)
    else: x = f'{nx}/{dx}'
    if dy == 0: y = "don't know"
    elif ny % dy == 0: y = str(ny//dy)
    else: y = f'{ny}/{dy}'

    # might redetermine x and y
    if a == b == 0 or (a, b, c) == (d, e, f):
        if d == 0 and e != 0:
            if f % e == 0:  y = str(f//e)
            else:           y = f'{f}/{e}'
        if e == 0 and d != 0:
            if f % d == 0:  x = str(f//d)
            else:           x = f'{f}/{d}'
    if d == e == 0:
        if a == 0 and b != 0:
            if c % b == 0:  y = str(c//b)
            else:           y = f'{c}/{b}'
        if b == 0 and a != 0:
            if c % a == 0:  x = str(c//a)
            else:           x = f'{c}/{a}'
    if a == b == 0 != c or d == e == 0 != f: x = y = "don't know"
    print(x)
    print(y)