from math import *
n = int(input()); s = {0:1}
for _ in range(n):
    _, *a = map(int, input().split()); t = {}
    for i in a:
        for j in s:
            if i+j not in t: t[i+j] = 0
            t[i+j] += s[j]
    s = t
z = sum(s.values())
for i in sorted(s): v = s[i]; d = gcd(v, z); print(i, f'{v//d}/{z//d}')