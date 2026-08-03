import sys; input = sys.stdin.readline
from cmath import *
N = int(input()); P = {}; A = []; W = []; prv = S = Z = 0; gr = (5**0.5-1)/2; tol = 1e-9
for i in range(N):
    a, e, f = map(float, input().split())
    W += [(e, f)[a<180]]; S += exp((90-a)*pi/180*1j)*W[i]
    A.append(a:=a*pi/180)
    P.setdefault(2*pi-a, []).append((f, i))
    P.setdefault((pi-a)%(2*pi) or 2*pi, []).append((e, i))
def f(x): return (S*exp(-x*1j)).real
for t in sorted(P):
    a, b = prv, t
    while b-a>tol:
        if f(μ:=(1-gr)*a+gr*b) < f(λ:=gr*a+(1-gr)*b): b = μ
        else: a = λ
    Z = max(Z, f((a+b)/2))
    for u, i in P[t]: S += exp((pi/2-A[i])*1j)*(u-W[i]); W[i] = u
    prv = t
print(Z)