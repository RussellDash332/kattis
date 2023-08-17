import sys; input = sys.stdin.readline
from array import array
def p(bm, c, b):
    if c == 0: return 1
    if (key:=bm*17000+c*101+b) in mem: return mem[key]
    if bin(bm).count('1') < c != 0: mem[key] = 0; return mem[key]
    best = 0
    for i in range(n):
        if bm&(1<<i) and b >= cost[i]: nxt = bm^(1<<i); bb = b-cost[i]; best = max(best, prob[i]*p(nxt, c-1, bb)+(1-prob[i])*p(nxt, c, bb))
    mem[key] = best; return best
for _ in range(int(input())):
    n, c, b = map(int, input().split())
    cost = array('i', []); prob = array('f', [])
    for _ in range(n): m, f = map(int, input().split()); cost.append(m), prob.append(f/100)
    mem = {}; print(p((1<<n)-1, c, b))