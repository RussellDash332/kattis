from math import *
xm, vx, vy, xa, va, tk = map(int, input().split())
T = hypot(xm+vx*tk-xa, vy*tk-16*tk*tk)/va
r = acos((xm+vx*tk-xa)/va/T)*180/pi
if 0 < T < tk < vy/16: print(tk-T, r)
else: print('start running')