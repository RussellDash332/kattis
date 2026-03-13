def f(n):
    return sum(c[i]*n**i for i in range(N-1))*n-d*n**N
N, *c, d = map(int, open(0).read().split())
a, b = 0, 1e4
gr = (5**0.5-1)/2
tol = 1e-9
while b-a>tol:
    if f(μ:=(1-gr)*a+gr*b) < f(λ:=gr*a+(1-gr)*b): b = μ
    else: a = λ
print((a+b)/2)