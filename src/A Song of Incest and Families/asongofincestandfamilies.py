M = {}; Q = 0
class P:
    def __init__(s, n, m, f, g):
        s.n = n; s.m = s.f = None; s.g = g
        if m: s.m = m
        if f: s.f = f
        s.c = {}; s.k = set(); s.t = {}
    def __repr__(s): return f'(n={s.n}, g={s.g}, m={s.m and s.m.n}, f={s.f and s.f.n})'
for _ in range(int(input())):
    v = input().split()
    if 'giftust' in v:
        a, _, b, *_ = v
        if a == '?': a = '?'+str(Q:=Q+1)
        if b == '?': b = '?'+str(Q:=Q+1)
        if a not in M: M[a] = P(a, None, None, 0)
        if b not in M: M[b] = P(b, None, None, 1)
        a = M[a]; b = M[b]
        a.k.add(b); b.k.add(a)
        a.c[b] = []; b.c[a] = []
    else:
        a, _, b, _, g, c, _ = v
        if a == '?': a = '?'+str(Q:=Q+1)
        if b == '?': b = '?'+str(Q:=Q+1)
        if a not in M: M[a] = P(a, None, None, 0)
        if b not in M: M[b] = P(b, None, None, 1)
        a = M[a]; b = M[b]; M[c] = P(c, b, a, int('p' in g)); c = M[c]
        if b in a.c: a.c[b] += [c]; b.c[a] += [c]
        else:
            if b not in a.t: a.t[b] = []; b.t[a] = []
            a.t[b] += [c]; b.t[a] += [c]
for _ in range(int(input())):
    a, b = input().split(); a = M[a]; b = M[b]; Z = []
    if a == b: Z += ['ég'] # self
    if b in a.k:
        if b.g: Z += ['eiginkona'] # wife
        else: Z += ['eiginmaður'] # husband
    if (b in a.t and a.t[b]) or (b in a.c and a.c[b]):
        if b.g: Z += ['barnsmóðir'] # child's mother
        else: Z += ['barnsfaðir'] # child's father
    if a in (b.f, b.m):
        if b.g: Z += ['dóttir'] # daughter
        else: Z += ['sonur'] # son
    if b == a.f: Z += ['faðir'] # father
    if b == a.m: Z += ['móðir'] # mother
    if a != b and (a.f == b.f != None)!=(a.m == b.m != None):
        if b.g: Z += ['hálfsystir'] # half-sister
        else: Z += ['hálfbróðir'] # half-brother
        Z += ['hálfsystkini'] # half-sibling
    # (great)*grand(father/mother)
    Q = [(a, 0)]; fs = 0
    for u, d in Q:
        if a != u == b: fs = d
        if a != u == b and d>1: Z += ['a'.join(['lang']*(d-2))+('amma' if b.g else 'afi')]
        if u.m: Q += [(u.m, d+1)]
        if u.f: Q += [(u.f, d+1)]
    if fs:
        if b.g: Z += ['formóðir'] # foremother
        else: Z += ['forfaðir'] # forefather
    # [(great)*grand]child
    Q = [(b, 0)]; ds = 0
    for u, d in Q:
        if b != u == a and d: Z += ['a'.join(['barn']*d)]; ds = 1
        if u.m: Q += [(u.m, d+1)]
        if u.f: Q += [(u.f, d+1)]
    if ds: Z += ['afkomandi'] # descendant
    if any(b==w.f for w in a.k): Z += ['tengdafaðir'] # father-in-law
    if any(b==w.m for w in a.k): Z += ['tengdamóðir'] # mother-in-law
    tm = a.m; tf = a.f
    for dc in (tm.c, tm.t):
        if tf not in dc: continue
        for c in dc[tf]:
            if c == a: continue
            if c == b:
                if b.g: Z += ['systir'] # sister
                else: Z += ['bróðir'] # brother
                Z += ['systkini'] # sibling
            for k in c.k:
                if k == b:
                    if b.g: Z += ['mágkona'] # sister-in-law (wife of sibling)
                    else: Z += ['mágur'] # brother-in-law (wife of sibling)
    for w in a.k:
        for dc in (w.m.t, w.m.c):
            if w.f not in dc: continue
            for c in dc[w.f]:
                if w != c == b:
                    if b.g: Z += ['mágkona'] # sister-in-law (sister of wife/husband)
                    else: Z += ['mágur'] # brother-in-law (brother of wife/husband)
    for dc in (a.t, a.c):
        for cc in dc.values():
            for c in cc:
                if b in c.k:
                    if b.g: Z += ['tengdadóttir'] # daughter-in-law
                    else: Z += ['tengdasonur'] # son-in-law
    # k-th cousin, 1<=k<=L-2
    L = 22
    da = [set() for _ in range(L)]; db = [set() for _ in range(L)]
    da[0] = {a}; db[0] = {b}
    for i in range(1, L):
        for u in da[i-1]:
            if u.m: da[i].add(u.m)
            if u.f: da[i].add(u.f)
        for u in db[i-1]:
            if u.m: db[i].add(u.m)
            if u.f: db[i].add(u.f)
    if all(b not in da[i] for i in range(L)) and all(a not in db[i] for i in range(L)):
        for i in range(L):
            if da[i]&db[i]:
                if i>1: Z += [['tví','þrí','fjór','fimm','sex','sjö','átta','níu','tíu','ellefu','tólf','þrettán','fjórtán','fimmtán','sextán','sautján','átján','nítján','tuttugu'][i-2]+'menningur']
                break
    for w in a.k:
        for dc in (w.m.t, w.m.c):
            if w.f in dc:
                for c in dc[w.f]:
                    if c != w:
                        for k in c.k:
                            if a != k == b:
                                if b.g: Z += ['svilkona'] # sister-in-law (wife of brother of wife/husband)
                                else: Z += ['svili'] # brother-in-law (husband of sister of husband/wife)
    if all(u not in Z for u in ['ég', 'systkini', 'hálfsystkini', 'forfaðir', 'formóðir', 'afkomandi']):
        if any(da[i]&db[j] for i in range(L) for j in range(L)):
            if b.g: Z += ['frænka'] # aunt/niece/cousin
            else: Z += ['frændi'] # uncle/nephew/cousin
    for dc in (a.k, a.t):
        for w in dc:
            if a != b and ((w in a.t and a.t[w]) or (w in a.c and a.c[w])) and ((w in b.t and b.t[w]) or (w in b.c and b.c[w])):
                if w.g: Z += ['kviðmágur'] # belly brother
                else: Z += ['sprotasystir'] # belly sister
    Z = sorted({*Z})
    print(len(Z))
    for i in Z: print(i)