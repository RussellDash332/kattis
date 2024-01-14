import sys
from collections import *
q = [Counter()]
for l in sys.stdin:
    l = l.strip()
    if not l or l == '<text>': continue
    if l == '</text>':
        q.append(Counter())
        if len(q) > 8: q.pop(0)
    elif l[:3] == '<to':
        n = int(l[4:-2])
        h = Counter()
        for c in q:
            for w in c: h[w] += c[w]
        s = sorted(h.items(), key=lambda x: (-x[1], x[0]))
        print(f'<top {n}>')
        n = min(n, len(s))
        for x in s:
            if x[1] >= s[n-1][1]: print(*x)
        print('</top>')
    else:
        for w in l.split():
            if len(w) > 3: q[-1][w] += 1