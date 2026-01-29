class Surd:
    def __init__(s, a=0, b=0):
        s.a = a%M; s.b = b%M
    def __add__(s, o):
        return Surd(s.a+o.a, s.b+o.b)
    def __sub__(s, o):
        return Surd(s.a-o.a, s.b-o.b)
    def __mul__(s, o):
        return Surd(s.a*o.a+5*s.b*o.b, s.a*o.b+s.b*o.a)
    def __pow__(s, p):
        z = Surd(1); b = s
        while p:
            if p%2: z *= b
            b *= b; p >>= 1
        return z
    def inv(s):
        e = pow((s.a**2-5*s.b**2)%M, -1, M); return Surd(s.a*e, -s.b*e)
M = 10**9+7; n, k = map(int, input().split()); h = pow(2, -1, M); a = Surd(h, h); b = Surd(h, -h); f = [1]
for i in range(k): f += [f[-1]*-~i%M]
g = [pow(x, -1, M) for x in f]; z = Surd()
for i in range(k+1): r = a**i*b**(k-i); z += Surd(1-(k-i)%2*2)*Surd(f[k]*g[i]*g[k-i])*(Surd(n+1) if r.a == 1 > r.b else (r**(n+1)-Surd(1))*(r-Surd(1)).inv())
print((z*(Surd(0, 1)**k).inv()).a)