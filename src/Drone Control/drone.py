for _ in range(int(input())):
    P, R, Y = map(float, input().split())
    def f(x):
        return max(map(abs, [x, (R+Y+P)/2-x, x-R, (R+Y-P)/2-x]))
    a, b = -2, 2; gr = (5**0.5-1)/2; tol = 1e-6
    while b-a>tol:
        if f(μ:=(1-gr)*a+gr*b) > f(λ:=gr*a+(1-gr)*b): b = μ
        else: a = λ
    print(x:=(a+b)/2, (R+Y+P)/2-x, x-R, (R+Y-P)/2-x)