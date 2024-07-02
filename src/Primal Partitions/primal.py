import sys; input = sys.stdin.readline; from math import *
N, K = map(int, input().split()); A = [*map(int, input().split())]; LIMIT = 10**6+1; spf = [*range(LIMIT)]; p = 2; lpf = [*spf]; lpf[1] = 0
while p < LIMIT:
    if spf[p] == p:
        for i in range(p*p, LIMIT, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
for i in range(2, LIMIT):
    n = i
    while n != 1:
        p = spf[n]
        while n%p == 0: n //= p
    lpf[i] = p

def f(p):
    z = 1; m = A[0]
    for i in A:
        if lpf[m:=gcd(m, i)] < p: z += 1; m = i
    return z <= K

lo, hi = 0, LIMIT
while hi-lo>1:
    if f(mi:=(lo+hi)//2): lo = mi
    else: hi = mi-1
print(hi if f(hi) else hi-1)