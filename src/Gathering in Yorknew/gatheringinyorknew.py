import sys; input = sys.stdin.readline; from array import *; from bisect import *
N = int(input()); xP = []; xN = []
for i in map(int, input().split()):
    if i > 0: xP.append(i)
    elif i < 0: xN.append(-i)
xP = array('i', sorted(xP)); xN = array('i', sorted(xN)); a = c = 0; b = d = 2*10**9+1; fP = [s:=0]+[(s:=s+i) for i in xP]; fN = [s:=0]+[(s:=s+i) for i in xN]
def f(k): return 2*(fP[z1:=bisect(xP, k/2)]-fP[z2:=bisect(xP, k)])+k*(2*z2-z1-len(xP))
def g(k): return 2*(fN[z1:=bisect(xN, k/2)]-fN[z2:=bisect(xN, k)])+k*(2*z2-z1-len(xN))
while b-a>2:
    if f(μ:=b-(b-a)//3) >= f(λ:=a+(b-a)//3): b = μ
    else: a = λ
while d-c>2:
    if g(μ:=d-(d-c)//3) >= g(λ:=c+(d-c)//3): d = μ
    else: c = λ
print(min(f(min(range(a-2, b+3), key=f)), g(min(range(c-2, d+3), key=g)))+fP[-1]+fN[-1])