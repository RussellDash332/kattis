import sys
for p in sys.stdin:
    p = p.strip()
    s = sum(map(int, p))
    if s % len(p): print(f'{p}: invalid # of balls')
    else:
        b = s // len(p)
        h = [0]*len(p)
        ok = 1
        for t, i in enumerate(map(int, p)):
            v = (t+i) % len(p)
            if h[v]: ok = 0; break
            h[v] = 1
        if ok: print(f'{p}: valid with {b} balls')
        else: print(f'{p}: invalid pattern')