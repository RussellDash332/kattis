import sys; input = sys.stdin.readline
LIMIT = 10**6
spf = list(range(LIMIT+1))
p = 2; P = [0]
while p <= LIMIT:
    if spf[p] == p:
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
for n in range(1, LIMIT+1):
    c1 = c2 = c3 = c4 = 1
    while n != 1:
        pp = spf[n]; k = 0
        while n % pp == 0: n //= pp; k += 1
        c1 *= 2*k*k+2*k+1; c2 *= 2*(k//3)+1; c3 *= 2*(k//2)+1; c4 *= 2*k+1
    P.append(P[-1]+c1-4*c2-2*c3-2*c4+7)
for _ in range(int(input())): n = int(input()); r = int(n**(1/3)); print(P[r+((r+1)**3<=n)])