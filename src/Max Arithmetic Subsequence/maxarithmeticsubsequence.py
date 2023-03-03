from random import *
for _ in range(int(input())):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    sarr, fin = set(arr), -1
    for _ in range(150):
        idx = randint(0, n-1)
        while True:
            shift = randint(-c, c)
            if shift != 0 and 0 <= idx+shift < n: break
        s = e = arr[idx]
        diff = abs(arr[idx+shift]-s)
        while s-diff in sarr: s -= diff
        while e+diff in sarr: e += diff
        sub = (e-s)//diff + 1
        if sub > n/c: fin = max(fin, sub)
    print(fin)