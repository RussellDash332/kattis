import sys; input = sys.stdin.readline; sys.setrecursionlimit(11**4); reg = {}
def parse(l, r):
    if e[l] == '"': return e[l+1:r-1]
    if e[l] != '`': return reg[e[l:r]]
    s = ''; p = l+1
    while p < r-1:
        if e[p] != '$' or (e[p] == '$' and e[p+1] != '{'):
            s += e[p]; p += 1
            if len(s) > 10**4: return '?'
        else:
            q = p+2; b = 1
            while b:
                if e[q] == '{': b += 1
                elif e[q] == '}': b -= 1
                q += 1
            s += parse(p+2, q-1); p = q
            if len(s) > 10**4 or (s and s[-1] == '?'): return '?'
    if len(s) > 10**4 or (s and s[-1] == '?'): return '?'
    return s
while (s:=input().strip()[:-1])[0] != 'e':
    if s[0] == 'v': vn, *e = s[4:].split(' = '); e = ' = '.join(e); reg[vn] = parse(0, len(e))
    else: e = s[6:]; print(parse(0, len(e)))