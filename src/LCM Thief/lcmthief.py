import sys; input = sys.stdin.readline
LIMIT = 10**6; spf = [*range(LIMIT+1)]; p = 2; primes = []
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2

def pf(n):
    res = []; k = 0
    while n != 1:
        pp = spf[n]
        while n % pp == 0: n //= pp; k += 1
        if k: res.append((pp, k))
        k = 0
    return res

n = int(input())
w = [int(input()) for _ in range(n)]; f = [pf(i) for i in w]
pp = {}
for i in f:
    for j, k in i:
        if j not in pp: pp[j] = []
        pp[j].append(k)
        if len(pp[j]) > 2: pp[j].remove(min(pp[j]))
for i in pp:
    if len(pp[i]) < 2: pp[i].append(0)
    pp[i].sort()
best = (float('inf'), 0)
for v, p in zip(w, f):
    dv = 1
    for q, k in p:
        if pp[q][0] != k == pp[q][1]: dv *= q**(pp[q][1]-pp[q][0])
    best = min(best, (dv, v))
print(best[1])