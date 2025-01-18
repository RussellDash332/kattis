def split(v):
    if v >= 0: return divmod(v, 10)
    elif v%10 == 0: return (v//10, 0)
    return (v//10+1, v%10-10)

def clean(r):
    p = sorted(r); q = 0
    while q < len(p):
        if abs(r[p[q]]) > 9:
            c, s = split(r[p[q]]); r[p[q]] = s
            if p[q]+1 not in p: r[p[q]+1] = c; p.append(p[q]+1); p.sort()
            else: r[p[q]+1] += c
        q += 1
    return r

class Dec:
    def __init__(self, v):
        self.v = {i:v[i] for i in v if v[i]}
    def __add__(self, o):
        r = {}
        for i in self.v: r[i] = self.v[i]
        for i in o.v: r[i] = r.get(i, 0)+o.v[i]
        if r and max(map(abs, r.values())) > 9: r = clean({i:r[i] for i in r if r[i]})
        return Dec({i:r[i] for i in r if r[i]})
    def __sub__(self, o):
        r = {}
        for i in self.v: r[i] = self.v[i]
        for i in o.v: r[i] = r.get(i, 0)-o.v[i]
        if r and max(map(abs, r.values())) > 9: r = clean({i:r[i] for i in r if r[i]})
        return Dec({i:r[i] for i in r if r[i]})
    def __mul__(self, o):
        r = {}
        for i in self.v:
            for j in o.v: r[i+j] = r.get(i+j, 0)+self.v[i]*o.v[j]
        if r and max(map(abs, r.values())) > 9: r = clean({i:r[i] for i in r if r[i]})
        return Dec({i:r[i] for i in r if r[i]})
    def __lt__(self, o):
        r = (self-o).v
        return len(r) > 0 and r[max(r)] < 0
    def __eq__(self, o):
        r = (self-o).v
        return not r
    def __neg__(self):
        r = {}
        for i in self.v: r[i] = -self.v[i]
        return Dec({i:r[i] for i in r if r[i]})
    def __abs__(self):
        if self < ZERO: return -self
        return self

def parse(v):
    r = {}
    e = int(v[v.find('e')+1:])
    s = 1 if v[0] == '+' else -1
    E = 0
    for i in range(1, v.find('e')):
        if v[i] == '.': continue
        if int(v[i]): r[E+e] = s*int(v[i])
        E -= 1
    return r

x, y, a, b, c, d = (Dec(parse(input())) for _ in range(6))
eps = Dec({-9: 1}); ZERO = Dec({})

def check(stu, cor):
    ae = stu-cor
    if abs(ae) == eps or abs(ae) > eps: return 0
    if cor == ZERO: return ae == ZERO
    return abs(ae) < abs(eps*cor)

def check2(d, x, y):
    ae = d*y-x
    if abs(ae) == abs(eps*y) or abs(ae) > abs(eps*y): return 0
    return abs(ae) < abs(eps*x)

print(['Incorrect', 'Correct'][check(a, x+y)])
print(['Incorrect', 'Correct'][check(b, x-y)])
print(['Incorrect', 'Correct'][check(c, x*y)])
print(['Incorrect', 'Correct'][check2(d, x, y)])