from collections import *
class A:
    ot = []
    def __init__(self, b): self.b = b; self.c = Counter(); self.ot.append(self)
def conn(a, b): a.c[b] += 1; b.c[a] += 1
def prep(s): return [A('.FONC'.index(i)) if i in 'CFNO' else i for i in s]
def parse(s, t={}, p=None):
    u = []; z = 0
    while z < len(s):
        i = s[z]
        if type(i)==A: p and conn(i, p); u.append(p:=i)
        elif i=='(':
            v = []; z += 1; b = 1
            while b: v.append(s[z]); b += (s[z]=='(')-(s[z]==')'); z += 1
            z -= 1; parse(v[:-1], t, u[-1])
        elif '0'<i<='9':
            if i not in t: t[i] = u[-1]
            else: conn(t.pop(i), u[-1])
        elif i=='=': conn(p, s[z+1])
        else: u.append(i)
        z += 1
parse(prep(input())); Z = []
for a in A.ot:
    if a.b == 2 and sum(a.c.values()) == 1:
        x = [*a.c][0]
        if max(x.c.values()) == 1 and x.b == 4: Z += [max(sum(h.b==4 for h in x.c), 1)]
print(*(sorted({*Z}) or [0]))