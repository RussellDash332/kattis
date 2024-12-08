n, m, k = map(int, input().split()); k -= 1
v = [int(input()) for _ in range(n)]
r = {*(v[:k]+v[k+1:])}
c = []
for _ in range(m): o, x = input().split(); c.append((o, int(x)))
q = [(v[k], 0, [])]
for w, d, p in q:
    if w not in r: print(d, *p); exit(0)
    for i in range(m):
        o, x = c[i]
        if o == '-':
            if x <= w: q.append((w-x, d+1, p+[i+1]))
        elif o == '+': q.append((w+x, d+1, p+[i+1]))
        elif o == '*': q.append((w*x, d+1, p+[i+1]))
        elif o == '/' and x: q.append((w//x, d+1, p+[i+1]))
print(-1)