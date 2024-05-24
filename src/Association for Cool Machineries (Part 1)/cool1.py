import sys; input = sys.stdin.readline; from array import *
n = int(input()); s = input().strip(); m = [input().strip() for _ in range(n)]; k = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}; s = [k[x] for x in s]; z = 0; w = array('i', ii:=[-1]*(n**3)); v = []
for t in range(n*n):
    if m[t//n][t%n] == 'R': break
while True:
    r = t//n; c = t%n; x = z%len(s); tt = t*n+x
    if w[tt] != -1: break
    w[tt] = z
    if m[r+s[x][0]][c+s[x][1]] != '#': v.append((z, s[x])); t = (r+s[x][0])*n+c+s[x][1]
    z += 1
v2 = [x[1] for x in v if x[0] >= w[tt]]
for i in range(1, len(v2)+1):
    if len(v2)%i: continue
    ok = 1
    for j in range(len(v2)//i):
        for k in range(i):
            if v2[k] != v2[i*j+k]: ok = 0; break
        if not ok: break
    if ok: print(i), exit(0)
print(1)