from copy import *
n = int(input()); r = [1, [], []]
def mul2(t):
    if t: t[0] *= 2; mul2(t[1]), mul2(t[2])
def add1(t, l):
    if t: t[0] += bool(t[1])^l; add1(t[1], l), add1(t[2], l)
for _ in range(n-1): r = [1, deepcopy(r), deepcopy(r)]; mul2(r[1]), mul2(r[2]), add1(r[1], 0), add1(r[2], 1)
ans = []
def trav(t):
    if t: ans.append(t[0]), trav(t[1]), trav(t[2])
trav(r), print(*ans)