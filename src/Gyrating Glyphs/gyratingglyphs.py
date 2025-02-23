from random import *; M = 10**9+7; B = 15
n = int(input()); b = [None]*(n+1); a = [0]*(n+1); P = 1; Q = 0
for i in range(n//B*B, -1, -B):
    for j in range(i, min(i+B, n+1)): a[j] = randint(1, M-1)
    print('?', *a); v = (P*int(input())+Q)%M; k = min(i+B, n+1)-i
    for c in range(1<<k):
        x = 0
        for j in range(k):
            if c&(1<<j): x = x*a[i+j]%M
            else: x = (x+a[i+j])%M
        if x == v: break
    for j in range(k-1, -1, -1):
        b[p:=i+j] = int(c&(1<<j)>0)
        if b[p]: w = pow(a[p], -1, M); P = P*w%M; Q = Q*w%M
        else: Q = (Q-a[p])%M
print('!', ''.join('+x'[i] for i in b[1:]))