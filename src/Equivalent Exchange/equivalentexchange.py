import sys

def flatten(l): # recursive flatten sucks
    r = []
    while l:
        u = l.pop()
        if type(u) != list: r.append(u)
        else:
            while u: l.append(u.pop())
    return r[::-1]

d, res = {}, []
input()
for l in sys.stdin:
    t, *i = map(int, l.split())
    if t == 1:
        i = int(i[0])
        if i not in d: d[i] = []
        d[i].append(len(res)), res.append(0)
    else:
        a, b = map(int, i)
        if a != b:
            if a not in d: d[a] = []
            if b not in d: d[b] = []
            d[b].append(d[a])
            d[a] = []
for k, v in d.items():
    for vv in flatten(v): res[vv] = k
for i in res: print(i)