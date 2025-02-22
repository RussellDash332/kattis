n, *t = map(int, open(0).read().split())
def f(x): return sum(abs(t[i]-x-i) for i in range(n))
a, b = -3*10**5, 3*10**5
while b-a>2:
    if f(μ:=b-(b-a)//3) > f(λ:=a+(b-a)//3): b = μ
    else: a = λ
print(min(f(i) for i in range(a-2, b+3)))