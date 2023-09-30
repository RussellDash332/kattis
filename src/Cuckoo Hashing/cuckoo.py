import sys; input = sys.stdin.readline
for _ in range(int(input())):
    m, n = map(int, input().split())
    h1 = []; h2 = []; t = [None]*n; ok = 1
    for i in range(m):
        a, b = map(int, input().split())
        if not ok: continue
        h1.append(a), h2.append(b)
        if t[a] == None: t[a] = i
        elif t[b] == None: t[b] = i
        else:
            t[a], r, x = i, t[a], a; ok = c = 0
            while c < 2:
                if r == i: c += 1 # cycle detected
                if r == None: ok = 1; break # assignment complete
                hh = h2 if x == h1[r] else h1
                t[hh[r]], r, x = r, t[hh[r]], hh[r]
    print(['rehash necessary', 'successful hashing'][ok])