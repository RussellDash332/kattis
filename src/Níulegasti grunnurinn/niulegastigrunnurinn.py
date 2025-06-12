def f(a, b, c):
    c -= n; d = b*b-4*a*c
    if d < 0 or (r:=int(d**.5))**2 != d: return 0
    e = -b+r; return e%(2*a)==0<=e!=e//(2*a)>max(a,b,c+n)
n, d = map(int, input().split())
if n <= d: print(int(n==d)); exit()
z = 3*f(d,d,d) or 2*int(n%d==0!=d+1<n//d) or int(n>2*d)
for i in range(max(2, d+1), 10**6+3):
    c = 0; m = n
    while m: c += m%i == d; m //= i
    if z < c: z = c
if z < 2 and d > 10**6:
    for i in range(10**5+3): # :)
        if (i and f(i,d,d)) or f(d,i,d) or f(d,d,i): z = 2; break
print(z)