(a,b),(c,d),(e,f),(g,h)=sorted(sorted(map(int,input().split()))[::-1]for _ in'....')[::-1];s=a*b+c*d+e*f+g*h
if(z:=round(s**0.5))**2!=s:print(0),exit(0)
if a==z: # there are some redundant cases but I decided to not care, brute-force it anyway
    if c+e+g==z:print(int(d==f==h==z-b))
    elif c+e+h==z:print(int(d==f==g==z-b))
    elif c+f+g==z:print(int(d==e==h==z-b))
    elif c+f+h==z:print(int(d==e==g==z-b))
    elif d+e+g==z:print(int(c==f==h==z-b))
    elif d+e+h==z:print(int(c==f==g==z-b))
    elif d+f+g==z:print(int(c==e==h==z-b))
    elif d+f+h==z:print(int(c==e==g==z-b))
    elif c==z-b==e+g:print(int(f==h==z-d))
    elif c==z-b==e+h:print(int(f==g==z-d))
    elif c==z-b==f+g:print(int(e==h==z-d))
    elif c==z-b==f+h:print(int(e==g==z-d))
    elif d==z-b==e+g:print(int(f==h==z-c))
    elif d==z-b==e+h:print(int(f==g==z-c))
    elif d==z-b==f+g:print(int(e==h==z-c))
    elif d==z-b==f+h:print(int(e==g==z-c))
    elif e==z-b==c+g:print(int(d==h==z-f))
    elif e==z-b==c+h:print(int(d==g==z-f))
    elif e==z-b==d+g:print(int(c==h==z-f))
    elif e==z-b==d+h:print(int(c==g==z-f))
    elif f==z-b==c+g:print(int(d==h==z-e))
    elif f==z-b==c+h:print(int(d==g==z-e))
    elif f==z-b==d+g:print(int(c==h==z-e))
    elif f==z-b==d+h:print(int(c==g==z-e))
    elif g==z-b==c+e:print(int(d==f==z-h))
    elif g==z-b==c+f:print(int(d==e==z-h))
    elif g==z-b==d+e:print(int(c==f==z-h))
    elif g==z-b==d+f:print(int(c==e==z-h))
    elif h==z-b==c+e:print(int(d==f==z-g))
    elif h==z-b==c+f:print(int(d==e==z-g))
    elif h==z-b==d+e:print(int(c==f==z-g))
    elif h==z-b==d+f:print(int(c==e==z-g))
    elif c==z:print(int((f==g==z-b-d or f==h==z-b-d or e==g==z-b-d or e==h==z-b-d)or(e==g==z)))
    else:print(0)
else:
    from itertools import permutations as q
    for(a,b),(c,d),(e,f),(g,h)in q([(a,b),(c,d),(e,f),(g,h)]):
        for a2,b2 in q((a,b)):
            for c2,d2 in q((c,d)):
                for e2,f2 in q((e,f)):
                    for g2,h2 in q((g,h)):
                        if a2+c2==f2+g2==b2+e2==d2+h2==z:print(1),exit(0)
    print(0)