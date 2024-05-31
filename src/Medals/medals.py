import sys; input = sys.stdin.readline; L = 2
while (n:=int(input())):
    h = {}; m = 0
    for _ in range(n): c, g, s, b = input().split(); h[c] = (int(g), int(s), int(b)); m += sum(h[c])
    if 'Canada' not in h: print('Canada cannot win.'); continue
    p = [m**i for i in range(L)]; ok = 0
    for j in range(L):
        if ok: break
        for k in range(L):
            if ok: break
            for l in range(L):
                z = {c:g*p[j]+s*p[k]+b*p[l] for c, (g, s, b) in h.items()}
                if max(z.values()) == z['Canada']: ok = 1; break
    print('Canada', ['cannot win.', 'wins!'][ok])