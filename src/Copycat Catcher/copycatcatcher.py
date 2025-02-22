from bisect import *
def f(c):
    s = []; h = {}
    for i in range(len(c)):
        if len(c[i]) == 1 and c[i].isalpha():
            if c[i] not in h: h[c[i]] = i
            s.append(str(i-h[c[i]])); h[c[i]] = i
        else: s.append(c[i])
    return ' '.join(s)
n = int(input()); q = input().split(); L = []
for i in range(n): L.append(f(q[i:]))
L.sort()
for _ in range(int(input())):
    input(); s = f(input().split())
    p = bisect_left(L, s)
    if p == len(L): print('no')
    else: print('yneos'[s!=L[p][:len(s)]::2])