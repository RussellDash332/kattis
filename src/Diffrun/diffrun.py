def parse_sgn():
    c = ''
    while q[0] < len(s):
        if s[q[0]] in '-+': c += s[q[0]]
        else: break
        q[0] += 1
    return c

def parse_num():
    c = ''
    while q[0] < len(s):
        if '0'<=s[q[0]]<='9': c += s[q[0]]
        else: break
        q[0] += 1
    return int(c) if c else 1

def parse_var():
    c = ''
    if q[0] < len(s):
        if 'a'<=s[q[0]]<='z': c = s[q[0]]; q[0] += 1
    if q[0] < len(s):
        if s[q[0]] in '^': c += s[q[0]]; q[0] += 1
    return c

s = input(); q = [0]
if s[0] not in '-+': s = '+'+s
t = [*s]; s = []
for i in t:
    if s and 'a'<=s[-1]<='z' and i!='^': s.extend('^1')
    if s and s[-1] in '+-' and 'a'<=i<='z': s.append('1')
    s.append(i)
if 'a'<=s[-1]<='z': s.extend('^1')
s = ''.join(s)
v = input()[-1]
t = []
def I(): return {'':0, **{chr(i+97):0 for i in range(26)}}
p = I()
while q[0] < len(s):
    sgn = parse_sgn()
    var = parse_var()
    exp = (1-2*((parse_sgn() or '+')=='-'))*parse_num()
    if sgn: t += [p]; p = I()
    p[var[:1]] += (1-2*(sgn=='-'))*exp
t += [p]
z = []
for u in t[1:]:
    if '' not in u: u[''] = 1
    if v in u:
        u[''] *= u[v]; u[v] -= 1
        for k in z:
            if all(k.get(chr(i+97), 0) == u.get(chr(i+97), 0) for i in range(26)): k[''] += u['']; break
        else: z.append(u)
s = ''
for i in sorted(z, key=lambda x: [-x.get(chr(i+97), 0) for i in range(26)]):
    for j in [*i]:
        if j and not i[j]: i.pop(j)
    if i[''] == 0: continue
    c = str(i['']) if (i[''] not in (-1, 1) or len(i)<2) else '-'*(i['']<0)
    for j in range(26):
        x = chr(j+97)
        if x in i: c += x+('^'+str(i[x]))*(i[x]!=1)
    if c[0]!='-': s += '+'+c
    else: s += c
print(s[s[:1]=='+':] or '0')