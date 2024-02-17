for _ in range(int(input())):
    x1, y1, z1, r1, vx1, vy1, vz1 = map(int, input().split())
    x2, y2, z2, r2, vx2, vy2, vz2 = map(int, input().split())
    a = (vx1-vx2)**2 + (vy1-vy2)**2 + (vz1-vz2)**2
    b = 2*((x1-x2)*(vx1-vx2) + (y1-y2)*(vy1-vy2) + (z1-z2)*(vz1-vz2))
    c = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 - (r1+r2)**2
    D = b*b-4*a*c
    if D < 0: print('No collision'); continue
    if a != 0:
        t1, t2 = (-b+D**0.5)/2/a, (-b-D**0.5)/2/a
        if t2 > 0: print(t2)
        elif t1 > 0: print(t1)
        else: print('No collision')
    elif b != 0:
        t = -c/b
        if t > 0: print(t)
        else: print('No collision')
    else:
        print('No collision')