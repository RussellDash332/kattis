import sys; input = sys.stdin.readline
from bisect import *
H = {}
for _ in range(int(input())):
    e, s, t = map(int, input().split())
    if e not in H: H[e] = []
    h = H[e]
    b = bisect(h, (s, t))
    if (b < len(h) and t >= h[b][0]) or (b and s <= h[b-1][1]): print('Starfsmadur er thegar a fundi'); continue
    insort(h, (s, t)); print('Fundur bokadur')