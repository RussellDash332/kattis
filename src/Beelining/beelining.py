from math import *
B, C = map(eval, input().split())
def f(n): return B**n+C/(n+1)
a, b = 0, log(10**10)/log(B)
gr = (5**0.5-1)/2
tol = 1e-9
while b-a>tol:
    if f(μ:=(1-gr)*a+gr*b) > f(λ:=gr*a+(1-gr)*b): b = μ
    else: a = λ
print(f((a+b)/2))