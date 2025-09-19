for s in input().replace(' ', '').split('()'):
    h = {}; z = []; b = 1
    if not s: break
    for t in s[1:-1].split(')('): k, v = t.split(','); h[v] = k
    for k in sorted(h, key=lambda x: (len(x), x)):
        if k[:-1] not in h: b = 0; break
        z.append(h[k])
    print(*[['incomplete'], z][b])