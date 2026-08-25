def ggcd(z1, z2):
    while z2 != (0, 0):
        x1, y1 = z1; x2, y2 = z2
        d = x2*x2+y2*y2; nx = x1*x2+y1*y2; ny = y1*x2-x1*y2; qx = (2*nx+d)//(2*d); qy = (2*ny+d)//(2*d)
        z1, z2 = z2, (x1-qx*x2+qy*y2, y1-qx*y2-qy*x2)
    return z1

import subprocess
from collections import Counter

def factorize(n):
    return Counter(map(int, subprocess.check_output(f"factor {n}",shell=1).split()[1:]))

N = int(input())
x, y = map(int, input().split()); z = (x, y)
for _ in range(N-1):
    x, y = map(int, input().split())
    z = ggcd(z, (x, y))
M = z[0]**2+z[1]**2; Z = 4
for k, v in factorize(M).items():
    if k%4==1: Z *= v+1
print(Z)