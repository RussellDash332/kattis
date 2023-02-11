from collections import deque
import sys

n, e = map(int, input().split())
g = {}
indeg = [0]*(e+1)
state = [0]*(e+1)
balls = [0]*(e+1)
u = 0
for line in sys.stdin:
    u += 1
    lr, i, j = line.split()
    i, j = int(i), int(j)
    indeg[i] += 1
    indeg[j] += 1
    state[u] = int(lr != 'L')
    g[u] = [i, j]

balls[1] = n
q = deque()
for i in range(e+1):
    if not indeg[i]: q.append(i)
topo = []
while q:
    u = q.popleft()
    topo.append(u)
    if u in g:
        for u2 in g[u]:
            indeg[u2] -= 1
            if not indeg[u2]: q.append(u2)
for i in topo[:-1]:
    b = balls[i]//2
    l, r = g[i]
    balls[l] += b
    balls[r] += b
    balls[g[i][state[i]]] += balls[i] % 2
    state[i] = (state[i] + balls[i]) % 2
print(''.join(map(lambda x: 'LR'[x], state[1:])))