def bt(v, cc):
    global Z, A
    if cc >= Z: return
    if v == n: Z = cc; A = [*cl]; return
    for i in range(1, cc+2):
        if cm[i]&am[v] == cm[i]:
            cl[v] = i; cm[i] |= 1<<v
            bt(v+1, max(cc, i))
            cm[i] ^= 1<<v; cl[v] = 0
n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m): a, b = map(int, input().split()); G[a] += [b]; G[b] += [a]
n = len(a:=G[1]); am = [0]*n
for i in range(n):
    am[i] |= 1<<i
    for j in range(n):
        if a[j] in G[a[i]]: am[i] |= 1<<j
Z, A = n+1, []; cl = [0]*n; cm = [0]*(n+1)
bt(0, 0)
T = {i:[] for i in range(1, Z+1)}
for i in range(n): T[A[i]].append(a[i])
print(Z)
for i in range(1, Z+1): print(len(k:=[1]+T[i]), *k)