import sys; input = sys.stdin.readline
m, h, c = {}, {}, {}
for _ in range(int(input())):
    d, t = input().strip().split(); d = int(d); m[d] = t
    for i in t:
        if i not in h: h[i] = []
        h[i].append(d)
for i in h:
    c[i] = set()
    for j in range(len(h[i])-1): c[i].add(h[i][j+1]-h[i][j])
    if not c[i]: c.pop(i)
    else: c[i] = c[i].pop()
print(min(c, key=lambda i: (-c[i], h[i][1], m[h[i][1]].index(i))))