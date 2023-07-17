def gcd(a, b):
    while b: a, b = b, a%b
    return a

import sys
N = int(input())
if N == 3: print(0, 1), print(1, 1), print(1, 0), exit(0)
M = N//4+1
X = 2*10**7
slopes = set()
s = 2
while len(slopes) < M:
    for dx in range(1, s):
        dy = s - dx
        d = gcd(dx, dy)
        slopes.add((dx//d, dy//d))
    s += 1
slopes = sorted(slopes, key=lambda x: -x[1]/x[0])
tx, ty = sum(i[0] for i in slopes), sum(i[1] for i in slopes)
sx, sy = -tx, 0
poly = []
for dx, dy in slopes: sx += dx; sy += dy; poly.append((sx+X, sy+X))
for dx, dy in map(lambda x: (x[0], -x[1]), slopes[::-1]): sx += dx; sy += dy; poly.append((sx+X, sy+X))
for dx, dy in map(lambda x: (-x[0], -x[1]), slopes): sx += dx; sy += dy; poly.append((sx+X, sy+X))
for dx, dy in map(lambda x: (-x[0], x[1]), slopes[::-1]): sx += dx; sy += dy; poly.append((sx+X, sy+X))
while len(poly) != N: poly.pop()
#print(f'polygon{tuple(poly)}')
sys.stdout.write('\n'.join(map(lambda x: f'{x[0]} {x[1]}', poly)))