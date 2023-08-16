x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
xv, yv, r = map(int, input().split())
'''
Does it hit particle 2?
Find t such that ||(x1+xv*t-x2, y1+yv*t-y2)|| = 2r
(x1-x2+xv*t)**2 + (y1-y2+yv*t)**2 - 4*r**2
= (xv**2 + yv**2)t**2 + 2*(xv*(x1-x2)+yv*(y1-y2))t + (x1-x2)**2+(y1-y2)**2-4*r**2 = 0
'''
a = xv**2 + yv**2
b = 2*(xv*(x1-x2)+yv*(y1-y2))
c = (x1-x2)**2+(y1-y2)**2-4*r*r
d = b*b-4*a*c
b2 = 2*(xv*(x1-x3)+yv*(y1-y3))
c2 = (x1-x3)**2+(y1-y3)**2-4*r*r
d2 = b2*b2-4*a*c2
if d < 0 and d2 < 0: print(5), exit(0)
elif d < 0: # will hit particle 3
    t = (-b2-d2**0.5)/(2*a)
    if t < 0: print(5), exit(0)
    vx, vy = x3-x1-xv*t, y3-y1-yv*t; sx, sy, px, py = x3, y3, x2, y2; v = [2, 4]
elif d2 < 0: # will hit particle 2
    t = (-b-d**0.5)/(2*a)
    if t < 0: print(5), exit(0)
    vx, vy = x2-x1-xv*t, y2-y1-yv*t; sx, sy, px, py = x2, y2, x3, y3; v = [1, 3]
else: # technically will touch both, so whoever is earlier will get hit
    t1 = (-b-d**0.5)/(2*a)
    t2 = (-b2-d2**0.5)/(2*a)
    if t1 < t2 or t2 < 0: vx, vy = x2-x1-xv*t1, y2-y1-yv*t1; sx, sy, px, py = x2, y2, x3, y3; v = [1, 3]
    elif t1 > t2 or t1 < 0: vx, vy = x3-x1-xv*t2, y3-y1-yv*t2; sx, sy, px, py = x3, y3, x2, y2; v = [2, 4]
    else: print(5), exit(0)
# Will (sx, sy) + t*(vx, vy) hit (px, py)?
a = vx**2 + vy**2
b = 2*(vx*(sx-px)+vy*(sy-py))
c = (sx-px)**2+(sy-py)**2-4*r**2
d = b**2-4*a*c
print(v[d<0 or d**0.5<b])