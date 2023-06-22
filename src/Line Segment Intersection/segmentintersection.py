import sys

input()
for l in sys.stdin:
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, l.split())
    a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1
    d, e, f = y4-y3, x3-x4, (y4-y3)*x3 - (x4-x3)*y3

    # a == b == 0 <-> (x1, y1) == (x2, y2) <-> the segment is a point
    if a == b == 0:
        # both are the same point
        if d == e == 0:
            if (x1, y1) == (x3, y3): print('%.2f %.2f'%(x1, y1))
            else: print('none')
        # the point lies on the other segment
        else:
            if d*x1 + e*y1 == f and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4): print('%.2f %.2f'%(x1, y1))
            else: print('none')
    elif d == e == 0:
        if a*x3 + b*y3 == c and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2): print('%.2f %.2f'%(x3, y3))
        else: print('none')
    else:
        # from this point, both segments are not single points
        # [ax+by=c, dx+ey=f] can have one solution, or multiple
        # => [adx+bdy=cd, adx+aey=af] [aex+bey=ce, bdx+bey=bf]
        # => [(bd-ae)y=(cd-af)] [(ae-bd)x=(ce-bf)]
        # => [y=(cd-af)/(bd-ae)] [x=(bf-ce)/(bd-ae)]
        det = b*d-a*e
        if det:
            # unique intersection
            x, y = (b*f-c*e)/det, (c*d-a*f)/det
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4):
                print(('%.2f %.2f'%(x, y)).replace('-0.00', '0.00'))
            else: print('none')
        else:
            # parallel case
            if a*f != c*d or b*f != c*e: print('none')
            else:
                # multiple solutions
                # either both segments are the exact same,
                #  or exactly one segment endpoint is within the other segment
                #  or they happen to be collinear but never intersect
                p, q = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))
                r, s = min((x3, y3), (x4, y4)), max((x3, y3), (x4, y4))
                if (p, q) == (r, s):    i1, i2 = p, q
                elif p <= r <= q:       i1, i2 = r, min(q, s)
                elif r <= p <= s:       i1, i2 = p, min(s, q)
                else:                   i1 = i2 = None
                if i1 == i2 and i1 != None: print('%.2f %.2f'%i1)
                elif i1:                    print('%.2f %.2f %.2f %.2f'%(*i1, *i2))
                else:                       print('none')