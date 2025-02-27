from decimal import *
getcontext().prec = 28
N = int(input()); P = []; X = 0; Z = 0
r2 = Decimal(2)**Decimal(.5)
r3 = Decimal(3)**Decimal(.5)
r6 = Decimal(6)**Decimal(.5)
for _ in range(N):
    s, n = input().split(); n = Decimal(n)
    if s[0] == 't': v = (int(n-1), n, 0)
    elif s[0] == 's': v = (int(n*(r6-r2)), n, 1)
    else: v = (2 if n < 2 else int(n*r3), n, 2)
    P.append(v); X ^= v[0]
for v, n, t in P:
    W = X^v; A, B, C = ((n-1, n/(1+2/r3), n/(2*r3)), (4*n/(r6+r2), n-1, (n-1)/2), (n*r3, n*r2, n-1))[t]; Z += W+1 <= A
    for w in range(int(W*(r6+r2)/4)-5, int(W*(r6+r2)/4)+5):
        if 1 <= w <= B and int(w*(r6-r2)) == W: Z += 1; break
    for w in range(int(W/r3)-5, int(W/r3)+5):
        if 1 <= w <= C and (2 if w < 2 else int(w*r3)) == W: Z += 1; break
print(Z)