import sys; input = sys.stdin.readline; sys.setrecursionlimit(20000)

def read():
    global t, p
    n = ''; t += 1; x = t
    while p < len(s) and s[p] > ',': n += s[p]; p += 1
    if p < len(s) and s[p] == '(':
        p += 1; l, l2, a = read(); p += 1; r, r2, b = read(); p += 1; z = f'{n}({l},{r})'; w = f'{n}({h[l2] if l2 in h else l},{h[r2] if r2 in h else r})'
        if w not in h: h[w] = x; return z, w, a+b+1
        else: t -= a+b+1; return h[w], h[w], 0
    else:
        z = n
        if z not in h: h[z] = x; return z, z, 1
        t -= 1; return h[z], h[z], 0

for _ in range(int(input())): p = t = 0; s = input().strip(); h = {}; sys.stdout.write(read()[0]+'\n')