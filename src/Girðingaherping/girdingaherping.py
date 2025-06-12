import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def cross(a, b): return (a.conjugate()*b).imag
def area(p):
    z = 0
    for i in range(N): z += cross(p[i], p[(i+1)%N])
    return abs(z)
def simple(P):
    S = []; V = [0]*N; P = P+[P[i-1] for i in range(N)]
    for i in range(N):
        if (P[i].real, P[i].imag) > (P[i+N].real, P[i+N].imag): P[i], P[i+N] = P[i+N], P[i]
    def check(i, j):
        if (c1:=cross(P[i]-P[i+N], P[i]-P[j+N])) < 0 or (c2:=cross(P[j]-P[j+N], P[j]-P[i+N])) > 0: return 0
        return P[i] != P[j] if c1 or c2 else not cross(P[i]-P[i+N], P[j]-P[j+N])
    def cmp(j): cp = cross(P[j]-P[i], P[j]-P[j+N]); return cp < 0 or cp == 0 and cross(P[i]-P[i+N], P[j]-P[j+N]) < 0
    for i in sorted(range(2*N), key=lambda x: (P[x].real, P[x].imag, -x)):
        if i < N:
            lo = 0; hi = len(S)
            while lo < hi:
                if cmp(S[mi:=(lo+hi)>>1]): hi = mi
                else: lo = mi+1
            S.insert(lo, i); V[i] = 1; x = S.index(i)
            if x != 0 and check(S[x-1], i) or x != len(S)-1 and check(i, S[x+1]): return 0
        elif V[i-N]:
            S.pop(x:=S.index(i-N)); V[i-N] = 0
            if x != 0 and x != len(S) and check(S[x-1], S[x]): return 0
    return 1
N = int(input()); P = []
for _ in range(N): x, y = map(int, input().split()); P.append(complex(x, y))
lo, hi = 0, 1e9; mn = min(range(N), key=lambda x: (P[x].real, P[x].imag)); ok = 0; A = area(P)
while abs(lo-hi) > 2e-6:
    Q = []; mi = (lo+hi)/2
    for i in range(N): a, b, c = P[i-1], P[i], P[(i+1)%N]; p = a+mi/abs(v1:=(b-a)*1j)*v1; r = b+mi/abs(v2:=(c-b)*1j)*v2; Q.append(p+cross(r-p, s:=c-b)/cross(q:=b-a, s)*q)
    if Q[(mn+1)%N].real < Q[mn].real-1e-9 or Q[mn-1].real < Q[mn].real-1e-9 or not simple(Q): hi = mi
    elif 2*area(Q) > A: lo = mi
    else: hi = mi; ok = 1
print(mi if ok else 'Omogulegt!')