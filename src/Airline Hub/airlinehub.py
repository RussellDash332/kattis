import sys
from math import *

def geodist(lat1, lon1, lat2, lon2):
    dlat, dlon = abs(lat2-lat1), abs(lon2-lon1)
    a = sin(dlat/2)**2 + sin(dlon/2)**2*cos(lat1)*cos(lat2)
    return atan2(sqrt(a), sqrt(1-a))

n = -1
for line in sys.stdin:
    if n == -1:
        pts, pts2, n = [], [], int(line)
        d = [0]*n
    else:
        lat, lon = map(float, line.split())
        pts2.append((lat, lon))
        pts.append((lat*pi/180, lon*pi/180))
        n -= 1
        if n == 0:
            for i in range(len(pts)):
                lat1, lon1 = pts[i]
                for j in range(i+1, len(pts)):
                    lat2, lon2 = pts[j]
                    gd = geodist(lat1, lon1, lat2, lon2)
                    d[i] = max(d[i], gd)
                    d[j] = max(d[j], gd)
            n = -1
            la, lo = min(enumerate(pts2), key=lambda x: (d[x[0]], -x[0]))[1]
            print('%.2f %.2f'%(la, lo))