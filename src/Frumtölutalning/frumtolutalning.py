# /primecount
def pc(n):
    if n < 2: return 0
    v,r,j=int(n**0.5),n-1,1
    h,l,u=[0]*(v+1),[0]*(v+1),[0]*(v+1)
    for p in range(2,v+1):l[p],h[p]=p-1,n//p-1
    for p in range(2,v+1):
        if l[p]==l[p-1]:continue
        t,e=l[p-1],min(v,n//(p*p))
        r-=h[p]-t
        for i in range(p+j,e+1,j):
            if u[i]:continue
            d,x=i*p,((i*p)>v)&1
            h[i]-=[h,l][x][[d,n//d][x]]-t
        for i in range(v,p*p-1,-1):l[i]-=l[i//p]-t
        for i in range(p*p,e+1,p):u[i]=1
        if p==2:j+=1
    return r

from random import randint
def mr(p):
    if not p%3 or not p%5 or not p%7 or not p%11 or not p%13 or not p%17 or not p%23 or not p%29 or not p%31 or not p%37 or not p%41 or not p%43 or not p%47 or not p%53 or not p%59 or not p%61 or not p%67 or not p%71 or not p%73 or not p%79 or not p%83 or not p%89 or not p%97 or not p%101 or not p%103 or not p%107 or not p%109 or not p%113 or not p%127 or not p%131 or not p%137 or not p%139 or not p%149 or not p%151 or not p%157 or not p%163: return 0
    d, s = p-1, 0
    while d%2 == 0: d //= 2; s += 1
    x = pow(randint(2, p-2), d, p)
    if x == 1 or x == p-1: return 1
    ok = 0
    for _ in range(s):
        x = x*x%p
        if x == 1: return 0
        if x == p-1: ok = 1; break
    return ok

a, b = map(int, input().split())
if b < 10**12: print(pc(b)-pc(a-1))
else:
    s = 0
    for i in range(a//2*2+1, b+1, 2): s += mr(i)
    print(s)