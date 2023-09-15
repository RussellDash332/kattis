import sys; input = sys.stdin.readline
from collections import deque
n = int(input()); w = [input().strip() for _ in range(n)]; a = [*map(int, input().split())]; g = [set() for _ in range(26)]; r = {e-1:i for i,e in enumerate(a)}
for i in range(n-1):
    for j in range(i+1, n):
        if w[i].startswith(w[j]) and r[i] < r[j]: print('NE'), exit(0)
        if w[j].startswith(w[i]) and r[i] > r[j]: print('NE'), exit(0)
        for k in range(min(len(w[i]), len(w[j]))):
            if w[i][k] != w[j][k]:
                if r[i] < r[j]: g[ord(w[i][k])-97].add(ord(w[j][k])-97)
                else:           g[ord(w[j][k])-97].add(ord(w[i][k])-97)
                break
indeg, top = [0]*26, []
for v in range(26):
    for w in g[v]: indeg[w] += 1
q = deque([i for i in range(26) if indeg[i] == 0])
while q:
    u = q.popleft()
    top.append(u)
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)
if len(top) != 26: print('NE')
else:
    print('DA')
    for i in range(26): indeg[top[i]] = i
    print(''.join(map(lambda x: chr(x+97), indeg)))