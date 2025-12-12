from math import *
for _ in range(int(input())):
    n, *a = map(int, input().split()); s = {0:1}
    for x in a:
        t = {}
        for i in range(1, x+1):
            for j in s:
                if i+j not in t: t[i+j] = 0
                t[i+j] += s[j]
        s = t
    z = [0]*max(s)
    for i in s: z[i-1] = s[i]
    print(*z)