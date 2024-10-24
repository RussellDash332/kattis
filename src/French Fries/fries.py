import sys; input = sys.stdin.readline
from cmath import *; from array import *

# Want to evaluate P(x) * (x/2 + 1/(2x))^T
# Aiming for partial (54/100) :)

def fft(v, inv=False):
    stack = [(2*len(v), v)]; tmp = []
    while stack:
        nb, v = stack.pop(); n, b = nb//2, nb%2
        if b == 0:
            if n == 1: tmp.append(v)
            else: stack.append((2*n+1, v)), stack.append((n, v[1::2])), stack.append((n, v[::2]))
        else:
            yo, ye = tmp.pop(), tmp.pop(); y, wj = [0]*n, 1; w = exp(-1j*(2-4*inv)*pi/n)
            for i in range(n//2): y[i] = ye[i]+wj*yo[i]; y[i+n//2] = ye[i]-wj*yo[i]; wj *= w
            tmp.append(y)
    return tmp[0]

def mult(p1, p2):
    if len(p2) < 4:
        # brute-force it
        q = [0]*(len(p1)+len(p2)-1)
        for i in range(len(p1)):
            for j in range(len(p2)): q[i+j] += p1[i]*p2[j]
        return q
    n = 2**(len(bin(m:=len(p1)+len(p2)-1))-2); fft1, fft2 = fft(p1+[0]*(n-len(p1))), fft(p2+[0]*(n-len(p2)))
    return [t.real/n for t in fft([fft1[i]*fft2[i] for i in range(n)], inv=True)][:m]

def mult_sparse(sp, p):
    q = [0]*(max(sp)+len(p))
    for i in sp:
        for j in range(len(p)): q[i+j] += p[j]
    return q

def polypow(p, n):
    while len(p) > 1 and abs(p[-1]) < 5e-12: p.pop()
    if n == 1: return p
    elif n%2: return mult(polypow(p, n-1), p)
    return mult(q:=polypow(p, n//2), q)

P, T, L = map(float, input().split()); P = round(P); T = round(T)
X = array('i', map(int, input().split()))
C = [0]*(max(X)+1)
for i in X: C[i] = 1
U = polypow([0.5, 0, 0.5], T)
print(sum(i>=L for i in (mult(U, C) if P*T > 10**8 else mult_sparse({*X}, U))))