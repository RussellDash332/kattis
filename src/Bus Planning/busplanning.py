import sys; input = sys.stdin.readline; from time import *

def kill(cl):
    cc = {}
    for i in range(n):
        if cl[i] == 0: continue
        if cl[i] not in cc: cc[cl[i]] = []
        cc[cl[i]].append(i)
    print(len(cc))
    for i in cc.values(): print(*map(lambda x: vv[x], i))
    exit(0)

def bt(cl, v, z):
    if time()-T > 0.05: kill(z[1])
    if v < n:
        for i in range(1, v+2):
            if len(d[i]) == c: continue
            cl[v] = i; d[i].append(v); ok = 1
            for j in range(len(d[i])-1):
                if am[d[i][j]][v] < 1: ok = 0; break
            if ok and max(cl) < z[0]: z = bt(cl, v+1, z)
            cl[v] = 0; d[i].pop()
    elif (m:=max(cl)) < z[0]: z = (m, [*cl])
    return z

n, m, c = map(int, input().split()); T = time()
am = [[1]*n for _ in range(n)]; vv = [input().strip() for _ in range(n)]; r = {}
for i in range(n): r[vv[i]] = i
for _ in range(m): a, b = input().strip().split(); am[r[a]][r[b]] = am[r[b]][r[a]] = 0
d = {i:[] for i in range(1, n+1)}; d[1].append(0)
kill(bt([1]+[0]*(n-1), 1, (n+1, None))[1])