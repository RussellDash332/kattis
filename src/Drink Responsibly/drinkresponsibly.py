import sys; input = sys.stdin.readline; from array import *
m, u, d = map(float, input().split()); h = []; ss = []; cc = []; u = round(u*60); m = round(m*100); d = round(d)
for _ in range(d): b, s, z, c = input().split(); h.append(b); ss.append(round(int(s)*eval(z)*60)); cc.append(round(float(c)*100))
q = [(1201*m+u, -1) for i in range(d) if cc[i] <= m and ss[i] <= u]; p = array('b', [-1]*1201*1001)
for mu, pp in q:
    if p[mu] != -1: continue
    mm = mu//1201; uu = mu%1201; p[mu] = pp
    if mm == uu == 0:
        x = [0]*d; y = 0
        while p[y] != -1: x[p[y]] += 1; y += 1201*cc[p[y]]+ss[p[y]]
        for j in range(d):
            if x[j]: print(h[j], x[j])
        exit(0)
    for j in range(d):
        if cc[j] <= mm and ss[j] <= uu: q.append((1201*(mm-cc[j])+uu-ss[j], j))
print('IMPOSSIBLE')