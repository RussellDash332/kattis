n, m, F = map(eval, input().split())
a, b = 0, n-1
def f(x):
    return (m-(F*x)**2)/(n-x)
while b-a>2:
    if f(μ:=b-(b-a)//3) < f(λ:=a+(b-a)//3): b = μ
    else: a = λ
print(f(max(range(max(a-2, 0), min(b+3, n)), key=f)))