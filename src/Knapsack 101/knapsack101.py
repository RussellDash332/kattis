n, p = map(int, input().split())
A = [*map(int, input().split())]
z = int(input()); C = 18; K = max(n-C, 0); D = n-K; H = {}
for c in range(K): z = z*pow(A[2*c], -1, p)%p
for b in range(1<<D):
    u = 0; v = 1
    for i in range(D):
        if b&(1<<i): u += 1; v = v*A[~i]%p
    H[(u, v)] = b
for b in range(1<<D):
    u = 0; v = 1
    for i in range(D):
        if b&(1<<i): u += 1; v = v*A[(~i)-D]%p
    t = (D-u, z*pow(v, -1, p)%p)
    if t in H: print('10'*K+bin(b)[2:].zfill(D)+bin(H[t])[2:].zfill(D)); exit()