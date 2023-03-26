from collections import deque

r, c = map(int, input().split())
sr, sc, er, ec = map(int, input().replace('(', '').replace(')', '').split())
s, e = (sr-1)*c + sc-1, (er-1)*c + ec-1
g, w, p = [[i] for i in range(r*c)], set(), []
for i in range(r):
    l = input().strip()
    for j in range(c):
        if l[j] == '#': w.add(i*c + j)
for _ in range(int(input())):
    pn, *ps = map(int, input().replace('(', '').replace(')', '').split())
    p.append([ps[2*i]*c + ps[2*i+1] - (c+1) for i in range(pn)])
    if len(p[-1]) != 1: p[-1].extend(p[-1][-2:0:-1])

P = [{x[t%len(x)] for x in p} for t in range(120)]
K = ((-1, 0), (0, -1), (1, 0), (0, 1))
for i in range(r):
    for j in range(c):
        for di, dj in K:
            if 0 <= i+di < r and 0 <= j+dj < c:
                if i*c+j not in w and (i+di)*c+j+dj not in w: g[i*c+j].append((i+di)*c+j+dj)

h = [set() for _ in range(r*c)]
pos = 0
for rr in range(r):
    for cc in range(c):
        x = rr
        while x*c + cc not in w:
            h[pos].add(x*c + cc)
            if x-1 >= 0: x -= 1
            else: break
        x = rr
        while x*c + cc not in w:
            h[pos].add(x*c + cc)
            if x+1 < r: x += 1
            else: break
        x = cc
        while rr*c + x not in w:
            h[pos].add(rr*c + x)
            if x-1 >= 0: x -= 1
            else: break
        x = cc
        while rr*c + x not in w:
            h[pos].add(rr*c + x)
            if x+1 < c: x += 1
            else: break
        pos += 1

ans, Q, vis = -1, deque([(0, s)]), set()
while Q:
    dd, vv = Q.popleft()
    if vv == e: ans = dd; break
    t = dd % 120
    if 3600*t+vv in vis: continue
    vis.add(3600*t+vv)
    if h[vv] & P[t]: continue
    for nn in g[vv]: Q.append((dd+1, nn))
print('IMPOSSIBLE' if ans == -1 else ans)