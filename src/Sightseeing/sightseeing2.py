import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
for _ in range(int(input())):
    N, T = map(int, input().split())
    W = [[] for _ in range(2*N+3)]
    for i in range(N):
        c, p, q, r, s = map(int, input().split()); T -= c
        W[2*i] += [(2*i+2, r), (2*i+3, s)]
        W[2*i+1] += [(2*i+2, p), (2*i+3, q)]
    dd, zz = 10**18, []
    for s in (0, 1):
        D = [10**18]*(2*N+3); D[s] = 0; P = [-1]*(2*N+3)
        for j in range(2*N):
            for k, w in W[j]:
                if D[k] > D[j]+w: D[k] = D[j]+w; P[k] = j
        if D[2*N+s] < dd:
            dd = D[2*N+s]; z = [2*N+s]
            while ~z[-1]: z += [P[z[-1]]]
            zz = z
    if dd > T: print('IMPOSSIBLE'); continue
    print(''.join('FB'[i%2] for i in zz[-2:0:-1]))