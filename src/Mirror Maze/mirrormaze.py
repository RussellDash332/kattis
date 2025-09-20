def bz(a, b):
    if a == 0 or b == 0: return 1, 1
    p, q = bz(b, a%b); return (q, p-a//b*q)
for s in [*open(0)][1:]:
    k, d = map(int, s.split())
    if k%2 < 1:
        if d%k < 1 < d//k: print(1, d//k-1)
        else: print('impossible')
        continue
    if d%2: print('impossible'); continue
    a, b = bz(k+1, k-1); a *= d//2; b *= d//2
    if b <= 0: t = -b//((k+1)//2)+1; b += t*(k+1)//2; a -= t*(k-1)//2
    if a <= 0: t = -a//((k-1)//2)+1; b -= t*(k+1)//2; a += t*(k-1)//2
    if a > 0 and b > 0: print(a, b)
    else: print('impossible')