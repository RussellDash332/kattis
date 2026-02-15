def bk(r, p, x):
    if not p and not x: return Z.add(tuple(sorted(r)))
    a = 0
    for i in p: u = i; break
    for i in x: u = i; break
    for w in [*p]:
        if w in g[u]: continue
        r.add(w); bk(r, p&g[w], x&g[w])
        if len(Z) > 1000: return
        r.discard(w); p.discard(w); x.add(w)

while True:
    Z = set()
    n, m = map(int, input().split())
    g = [set() for _ in range(n)]
    for _ in range(m): a, b = map(int, input().split()); a -= 1; b -= 1; g[a].add(b); g[b].add(a)
    bk(set(), {*range(n)}, set()); print(len(Z) if len(Z) < 1001 else 'Too many maximal sets of friends.')
    try: input()
    except: break