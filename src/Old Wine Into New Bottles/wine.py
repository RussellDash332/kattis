from time import *; from array import *
L = 440000; D = array('B', [0]*L); D[0] = 1; T = time()
for _ in range(int(input())):
    B = set(); w, n = map(int, input().split()); w *= 1000
    for _ in range(n): l, h = map(int, input().split()); B.add((l, h))
    if w >= L: print(0); continue
    for l, h in B:
        e = 0; d = h-l
        for x in range(w-l+1):
            if D[x]: e = 0
            else: e += 1
            if e <= d: D[x+l] = 1
        if time()-T > 0.5: break
    for i in range(w, -1, -1):
        if D[i]: print(w-i); break
    for i in range(1, L): D[i] = 0