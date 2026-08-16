import sys; input = sys.stdin.readline
from math import *
N = int(input()); R = 6371; C = 299792.458
lo, la = map(float, input().split())
X = R*cos(la*pi/180)*cos(lo*pi/180)
Y = R*cos(la*pi/180)*sin(lo*pi/180)
Z = R*sin(la*pi/180)
for _ in range(N): p, s, r, x = map(float, input().split()); a = 2*pi*x; q = p*pi/180; t = s*pi/180; xs = r*(cos(a)*cos(q)-sin(a)*cos(t)*sin(q)); ys = r*(cos(a)*sin(q)+sin(a)*cos(t)*cos(q)); zs = r*sin(a)*sin(t); print('no signal' if X*xs+Y*ys+Z*zs < R*R else hypot(X-xs, Y-ys, Z-zs)/C)