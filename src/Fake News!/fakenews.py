n, m = map(int, input().split()); s = [[] for _ in range(n)]
def parse(u):
    z = []
    for i in u:
        if '0'<i<'9': z.append(int(i)-1)
        elif i[0] in 'tfc': v = z.pop(); x = i[0]; z.append((v, 'tfc'.find(x)))
        else: z.append(i[0])
    return z
def check(t, a):
    p = 0; u = []
    for i in t:
        if type(i)==str:
            p, q = u.pop(); r = a//3**p%3 == q
            if i == 'a': x, y = u.pop(); v = r and (a//3**x%3 == y)
            elif i == 'x': x, y = u.pop(); v = r != (a//3**x%3 == y)
            else: v = not r
            u.append((9, 1-v))
        else: u.append(i)
    p, q = u[0]; return a//3**p%3 == q
for _ in range(m): k, *v = input().split(); s[int(k)-1].append(parse(v[::-1]))
for a in range(3**n):
    ok = 1
    for i in range(n):
        v = a//3**i%3; w = [check(t, a) for t in s[i]]
        if v != 2 and not w: continue
        if v == 0 and False in w: ok = 0; break
        if v == 1 and True in w: ok = 0; break
        if v == 2:
            if True not in w or False not in w: ok = 0; break
            if sorted(w, reverse=True) != w: ok = 0; break
    if ok: print('\n'.join(['truther', 'fabulist', 'charlatan'][a//3**i%3] for i in range(n))); exit()