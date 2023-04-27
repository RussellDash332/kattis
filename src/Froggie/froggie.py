l, w = map(int, input().split())
ois = []
for _ in range(l):
    o, i, s = map(int, input().split())
    ois.append([o, i, s*(1-2*(_%2)), [o], 1-2*(_%2)])
ois = ois[::-1]
p, udlr = input().split()
p, y = int(p), -1

for o, i, s, ll, lr in ois:
    if lr > 0:
        while ll[-1] + i < w: ll.append(ll[-1] + i)
    else:
        ll[0] = w-1-ll[0]
        while ll[-1] - i >= 0: ll.append(ll[-1] - i)
        ll.reverse()

safe = True
for t, m in enumerate(udlr):
    if m == 'U':    y += 1
    elif m == 'L':  p -= 1
    elif m == 'R':  p += 1
    else:           y -= 1
    if y == l: break
    if y != -1:
        o, i, s, ll, _ = ois[y]
        for d in ll:
            if not safe: break
            for ds in range(min(d+s, d), max(d+s, d)+1):
                if s != 0 and ds == d: continue
                if p == ds: safe = False
    if not safe: break
    for o, i, s, ll, _ in ois:
        ll2 = list(map(lambda x: x + s, ll))
        while ll2[-1] + i < w: ll2.append(ll2[-1] + i)
        ll2.reverse()
        while ll2[-1] - i >= 0: ll2.append(ll2[-1] - i)
        ll2.reverse()
        ll.clear(), ll.extend(filter(lambda x: x >= 0, ll2))
print(['squish', 'safe'][safe and y == l])