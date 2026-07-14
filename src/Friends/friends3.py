import os, sys
c = 0; X = []; F = X.append
for i in os.read(0, 6_767_676):
    if i > 47: c = c*10+i-48
    else: F(c); c = 0
N, L, Q = X[0], X[1], X[2]; Z = 0; U = N+2; M = {}; S = C = 0; P = -2; T = []; pts = X[3:U+1]; R = []; W = set(pts); W.add(-2); u = U+1
for _ in range(Q):
    c = X[u]; u += 1
    if c: R.append(None)
    else: A = X[u]; B = X[u+1]; u += 2; R.append((A, B)); W.add(A+1); W.add(B)
W = sorted(W); Wn = len(W); V = {v:i for i,v in enumerate(W)}; F = [0]*(Wn+1); lg = Wn.bit_length(); pw = [1<<b for b in range(lg, -1, -1)]
def upd(i, d):
    i += 1
    while i <= Wn: F[i] += d; i += i&(-i)
def get(i):
    i += 1; s = 0
    while i > 0: s += F[i]; i -= i&(-i)
    return s
def kth(k):
    p = 0
    for w in pw:
        if (n:=p+w) <= Wn and F[n] < k: p = n; k -= F[n]
    return p
def G(x): return get(V[x])
def H(x): upd(V[x], 1)
def D(x): upd(V[x], -1)
def Y(k): return W[kth(k+1)]
for i in sorted(pts):
    if i != P+S:
        if S: Z += S*S; M[P] = P+S-1; H(P); C += 1
        S = 1; P = i
    else: S += 1
Z += S*S; M[P] = P+S-1; H(P); C += 1; O = []
for q in R:
    if q == None: O.append(Z); continue
    A, B = q; b = M[a:=Y(p:=G(A+1)-1)]
    if b > A > a: Z += (A-a)**2+(b-A)**2; M[a] = A-1; H(A+1); M[A+1] = b; C += 1
    elif A > a: Z += (A-a)**2; M[a] -= 1
    elif A < b: Z += (b-A)**2; M[A+1] = M.pop(a); D(a); H(A+1)
    else: D(a); del M[a]; C -= 1
    Z -= (b-a+1)**2; S = G(B); a = b = B
    if S < C and (e:=Y(S)) == B+1: b = M.pop(e); D(e); C -= 1; Z -= (b-B)**2
    if S > 0 and M[s:=Y(S-1)] == B-1: a = s; Z -= (M.pop(s)-s+1)**2; D(s); C -= 1
    H(a); M[a] = b; C += 1; Z += (b-a+1)**2
sys.stdout.write(' '.join(map(str, O)))