import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; O = []; A = O.append
T = 0
while (T:=T+1):
    C, P, Q = map(int, input().split())
    if C < 1: break
    F = [*map(int, input().split())]; D = [10**9]*C*C; Z = [*D]
    for _ in range(P): a, b, d = map(int, input().split()); a -= 1; b -= 1; D[a*C+b] = D[b*C+a] = min(D[a*C+b], d)
    for k in sorted(range(C), key=F.__getitem__):
        for i in range(C):
            for j in range(C): D[i*C+j] = min(D[i*C+j], D[i*C+k]+D[k*C+j]); Z[i*C+j] = min(Z[i*C+j], D[i*C+j]+max(F[i],F[j],F[k]))
    A(T)
    for _ in range(Q): a, b = map(int, input().split()); z = Z[~-a*C+~-b]; A(z if z < 10**9 else -1)
sys.stdout.write(' '.join(map(str, O)))