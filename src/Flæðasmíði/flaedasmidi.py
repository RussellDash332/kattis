n, m = map(int, input().split()); M = 1024; E = []; V = [n+M+1]
def f(x, y):
    if x == y: return [x+n]
    mi = (x+y)//2; z = []
    for l, r in zip(f(x, mi), f(mi+1, y)):
        for _ in range(2): V[0] += 1; z.append(V[0]); E.append((V[0], l)); E.append((V[0], r))
    return z
P = f(1, M)
for i in range(n): E.append((i+1, P[i]))
for i in range(M-m): E.append((n+m+1+i, P[i+n]))
print(V[0], len(E))
for e in E: print(*e)