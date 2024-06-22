from collections import *; from math import gcd; from random import *

# rewrite to optimize
class Fraction:
    def __init__(self, n, d):
        if n < 0: n, d = -n, -d
        self.n = n; self.d = d
    def __lt__(self, ot):
        return self.n*ot.d < self.d*ot.n
    def __add__(self, ot):
        n = self.n*ot.d+self.d*ot.n
        d = self.d*ot.d
        g = gcd(n, d); return Fraction(n//g, d//g)
    def __mul__(self, ot):
        n = self.n*ot.n
        d = self.d*ot.d
        g = gcd(n, d); return Fraction(n//g, d//g)
    def __sub__(self, ot):
        n = self.n*ot.d-self.d*ot.n
        d = self.d*ot.d
        g = gcd(n, d); return Fraction(n//g, d//g)
    def __truediv__(self, ot):
        n = self.n*ot.d
        d = self.d*ot.n
        g = gcd(n, d); return Fraction(n//g, d//g)
    def __repr__(self):
        return str(self.n)
    def __eq__(self, ot):
        if type(ot) == int: return self.n == ot*self.d
        else: return self.n*ot.d == self.d*ot.n
    def __hash__(self):
        return hash((self.n, self.d))

def end(seq, T):
    sol = {i:[] for i in seq[-1]}
    for i in seq[-1]: sol[i].append(str(i))
    for i in range(len(seq)-2, -1, -1):
        cur = [*seq[i]]; prev = [*seq[i+1]]
        for j in seq[i+1]:
            if j in cur: cur.remove(j); prev.remove(j)
        if not cur:
            v = prev[0]; f = 1
            if v not in sol: sol[v] = []
            if 0 not in sol: sol[0] = []
            for ii in sol:
                if ii != prev[0] and sol[ii]:
                    v = ii
                    if prev[0]+v == v: sol[v].append(f'({sol[v].pop()}+{sol[prev[0]].pop()})'); f = 0; break
                    elif prev[0]*v == v: sol[v].append(f'({sol[v].pop()}*{sol[prev[0]].pop()})'); f = 0; break
                    elif prev[0]-v == v: sol[v].append(f'({sol[prev[0]].pop()}-{sol[v].pop()})'); f = 0; break
                    elif prev[0]/v == v: sol[v].append(f'({sol[prev[0]].pop()}/{sol[v].pop()})'); f = 0; break
            if not f: continue
            if prev[0]+v == v: sol[v].append(f'({sol[v].pop()}+{sol[prev[0]].pop()})')
            elif prev[0]*v == v: sol[v].append(f'({sol[v].pop()}*{sol[prev[0]].pop()})')
            elif prev[0]-v == v: sol[v].append(f'({sol[prev[0]].pop()}-{sol[v].pop()})')
            elif prev[0]/v == v: sol[v].append(f'({sol[prev[0]].pop()}/{sol[v].pop()})')
            continue
        v = cur[0]; a, b = prev; aa = sol[a].pop(); bb = sol[b].pop()
        if v not in sol: sol[v] = []
        if v == a+b: sol[v].append(f'({aa}+{bb})')
        elif v == a*b: sol[v].append(f'({aa}*{bb})')
        elif v == a-b: sol[v].append(f'({aa}-{bb})')
        elif v == b-a: sol[v].append(f'({bb}-{aa})')
        elif b != 0 and v == a/b: sol[v].append(f'({aa}/{bb})')
        elif a != 0 and v == b/a: sol[v].append(f'({bb}/{aa})')
    return sol[T][0]

# BFS
def solve(C, T, c, out=None):
    Q = deque([c])
    while Q:
        s = Q.popleft()
        if len(s) == 1:
            if s[0] in T:
                ps = []; cc = s
                while cc != -1: ps.append(cc); cc = P[cc]
                if out == None: return end(ps, s[0])
                else: return out[s[0]].replace('@', end(ps, s[0]))
            continue
        nxt = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                cc = [s[k] for k in range(len(s)) if k != i and k != j]; a = s[i]; b = s[j]
                nxt.append(tuple(sorted(cc+[a+b])) if cc else (a+b,))
                nxt.append(tuple(sorted(cc+[a*b])) if cc else (a*b,))
                nxt.append(tuple(sorted(cc+[a-b])) if cc else (a-b,))
                nxt.append(tuple(sorted(cc+[b-a])) if cc else (b-a,))
                if b != 0: nxt.append(tuple(sorted(cc+[a/b])) if cc else (a/b,))
                if a != 0: nxt.append(tuple(sorted(cc+[b/a])) if cc else (b/a,))
        shuffle(nxt)
        for v in nxt:
            if v not in P: P[v] = s; Q.append(v)

C, T = map(int, input().split()); T = Fraction(T, 1)
c = tuple(sorted(Fraction(int(x), 1) for x in input().split()))
if C < 6: P = {c:-1}; print(solve(C, [T], c)), exit(0)

# pray we can have the solution {6} in the form of op(x, {5}) or op({5}, x)
U = [*range(C)]; shuffle(U)
for i in U:
    c2 = c[:i]+c[i+1:]; P = {c2:-1}
    if (v:=solve(5, {T-c[i], T/c[i], T+c[i], c[i]-T, T*c[i], c[i]/T}, c2, out={
        T-c[i]: f'({c[i]}+@)',
        T/c[i]: f'({c[i]}*@)',
        T+c[i]: f'(@-{c[i]})',
        c[i]-T: f'({c[i]}-@)',
        T*c[i]: f'(@/{c[i]})',
        c[i]/T: f'({c[i]}/@)'
    })): print(v), exit(0)