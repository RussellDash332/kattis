n = int(input()); g = [[] for _ in range(n)]; t = [[] for _ in range(n)]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283]
for _ in range(n-1): a, b = map(int, input().split()); g[a-1].append(b-1), g[b-1].append(a-1)
s = [0]; s2 = []; r = [None]*n
while s:
    for i in s:
        r[i] = 1
        for x in g[i]:
            if not r[x]: s2.append(x), t[i].append(x)
    s, s2 = s2, []
dd = []; s = [(0, [0]*len(primes))]; s2 = []; r = [None]*n; r[0] = [0]*len(primes)
for i in range(n):
    d = {i}
    for _ in range(n):
        for j in d.copy(): d |= {*t[j]}
    dd.append(d)
while s:
    for i, w in sorted(s, key=lambda x: len(t[x[0]])):
        for x in sorted(g[i], key=lambda x: -len(t[x])):
            if r[x]: continue
            ok = 0; p = -1; ww = w.copy()
            while not ok:
                ok = 1; p += 1
                for i2 in range(n):
                    ww[p] += 1
                    if x != i2 and r[i2] and (x not in dd[i2]) and all(ww[ii] >= r[i2][ii] for ii in range(len(primes))): ok = 0; ww[p] -= 1; break
                    ww[p] -= 1
            ww[p] += 1; s2.append((x, ww)); r[x] = s2[-1][1]
    s, s2 = s2, []
if (debug:=False):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if j not in dd[i]: assert any(r[j][ii] < r[i][ii] for ii in range(len(primes))), (i, r[i], dd[i], j, r[j], dd[j])
            else: assert all(r[j][ii] >= r[i][ii] for ii in range(len(primes)))
m = [0]*len(primes); rr = [1]*n
for i in range(n):
    for j in range(len(primes)): m[j] = max(m[j], r[i][j])
q = {i:primes[-e-1] for e, (_, i) in enumerate(sorted((e, i) for i, e in enumerate(m)))}
for i in range(n):
    for j in range(len(primes)): rr[i] *= q[j]**r[i][j]
assert max(rr) <= 10**18; print(*rr)