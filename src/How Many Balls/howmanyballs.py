P, Q = map(int, input().split())
for s in range(2, 2*10**7):
    t = s*(s-1)//2
    if t*P%Q==0:
        p = t*P//Q; D = s*s-4*p
        if D >= 0 and (r:=round(D**.5))**2 == D:
            if (x:=(s-r)//2) <= 10**6: print(x, x+r); break
else: print('impossible')