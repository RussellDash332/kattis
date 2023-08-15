from random import *
from math import ceil
import sys; input = sys.stdin.readline
n = int(input()); t = ceil(n*int(input())/100)
if n == 1: print('possible'), exit(0)
p = [[*map(int, input().split())] for _ in range(n)]
for _ in range(250):
    (x1, y1), (x2, y2) = sample(p, 2)
    a, b, c = y1-y2, x2-x1, x1*(y2-y1)-y1*(x2-x1)
    tt = 0
    for x, y in p: tt += a*x+b*y+c == 0
    if tt >= t: print('possible'), exit(0)
print('impossible')