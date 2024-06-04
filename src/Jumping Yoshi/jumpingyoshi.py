import sys; input = sys.stdin.readline; from array import *
n = int(input()); a = [*map(int, input().split())]; hp = {}; hn = {}; g = [[] for _ in range(n)]; d = array('i', [0]+[-1]*(n-1)); q = array('i', [0])
for i in range(n):
    p = a[i]+i; n = i-a[i]
    if p not in hp: hp[p] = []
    if n not in hn: hn[n] = []
    hp[p].append(i); hn[n].append(i)
for i in hp:
    if i in hn:
        for j in hn[i]:
            for k in hp[i]: g[k].append(j); g[j].append(k)
for u in q:
    for v in g[u]:
        if d[v] == -1: d[v] = d[u]+1; q.append(v)
while d[-1] == -1: d.pop()
print(len(d)-1)