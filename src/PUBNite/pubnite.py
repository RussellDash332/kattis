xs, ys, ss, ri, rf, xa, ya, sa = map(int, open(0).read().split())
d = (xs-xa, ys-ya)
v = (d[0]**2+d[1]**2)**.5
if v <= rf or (v <= ri and sa >= ss): print(0), exit()
tr = min((ri-rf)/ss, v/sa)
d = (d[0]/v*sa, d[1]/v*sa)
T = 0
A = d[0]**2+d[1]**2-ss**2
B = 2*((xa-xs)*d[0]+(ya-ys)*d[1]+ri*ss)
C = (xa-xs)**2+(ya-ys)**2-ri**2
D = B*B-4*A*C
if D < 0 and A > 0: T = tr
elif A:
    t1, t2 = min(max((-B-D**.5)/2/A, 0), tr), min(max((-B+D**.5)/2/A, 0), tr)
    if A < 0: T = t1-t2
    else: T = tr-t2+t1
elif B:
    t = min(max(-C/B, 0), tr)
    if B > 0: T = tr-t
    else: T = t
elif C > 0: T = tr
print(max((((xa+d[0]*tr-xs)**2+(ya+d[1]*tr-ys)**2)**.5-rf)/sa,0)+T)