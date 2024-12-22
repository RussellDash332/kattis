from math import *
s, r, n, z = map(float, input().split()); n = round(n); z = round(z); ans = 0
for k in range(n+1):
    f = r/s
    if k*f*f*100 > z: continue
    if f <= 1/3: ans = k
    if 2 < k < 7 and (1-f)/sin(pi*(1-2/k)/2) >= 2*f/sin(2*pi/k): ans = k
    if k == 2 and f <= 1/2: ans = k
    if k == 1 and f <= 1: ans = k
print(ans)