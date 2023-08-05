m = [[*map(int, input().split())] for _ in range(7)]
for i in range(7):
    if sum(r[i] for r in m) == 0: print('IMPOSSIBLE'), exit(0) # trivial column check
p = ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Fluttershy', 'Rainbow Dash', 'Spike']
h = {i:[] for i in range(7)}
for i in range(7):
    for j in range(7):
        if m[i][j] == 1: h[j].append(p[i])
best = (8, [], {})
for a in h[0]:
    for b in h[1]:
        for c in h[2]:
            for d in h[3]:
                for e in h[4]:
                    for f in h[5]:
                        for g in h[6]:
                            x = [a, b, c, d, e, f, g, h]
                            hh = {}
                            for i in range(7):
                                if x[i] not in hh: hh[x[i]] = []
                                hh[x[i]].append(i)
                            z = max(map(len, hh.values()))
                            best = min(best, (z, x, hh))
print(d:=best[0]); h = best[2]
for _ in range(d):
    print(len(h))
    for p in [*h]:
        print(p, h[p].pop()+1)
        if not h[p]: del h[p]