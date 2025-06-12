import sys; input = sys.stdin.readline; from math import gcd
n, q = map(int, input().split()); P = {i:i for i in range(n)}; R = 0; M = 1
for _ in range(q):
    c, x = input().split(); x = int(x); k = len(P)
    if c == '+': R = (R+x)%n
    elif c == '?':
        if (x-R)%(n//k): print(-1); continue
        p = (x-R)%n//(n//k)*pow(M, -1, k)%k*(n//k); print(n-(-P[p])%n if p in P else -1)
    elif gcd(x, k) == 1: M = M*x%n; R = R*x%n
    else:
        Q = {j:(M*i+R)%n for i,j in P.items()}; P = {}; M = 1
        for i in Q:
            r = Q[i]*x%n
            if r not in P: P[r] = []
            P[r].append((i, (r-Q[i])%n))
        for i in P: P[i] = min(P[i], key=lambda x: x[1])[0]
        R = min(P); P = {i-R: P[i] for i in P}