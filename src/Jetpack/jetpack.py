from collections import deque
n, m = int(input()), [list(input().strip()) for _ in range(10)]
g, q, v, p = [[] for _ in range(10*n)], deque([9*n]), {9*n}, [-1]*(10*n)
for i in range(9):
    for j in range(n-1):
        if m[i][j] == m[i+1][j+1] == '.': g[i*n+j].append((i+1)*n+j+1)
for i in range(1, 10):
    for j in range(n-1):
        if m[i][j] == m[i-1][j+1] == '.': g[i*n+j].append((i-1)*n+j+1)
for i in [0, 9]:
    for j in range(n-1):
        if m[i][j] == m[i][j+1] == '.': g[i*n+j].append(i*n+j+1)
while q:
    u = q.popleft()
    for w in g[u]:
        if w not in v:
            v.add(w), q.append(w)
            p[w] = u
fp = []
for i in range(n-1, 10*n, n):
    path = [i]
    while path[-1] != -1: path.append(p[path[-1]])
    path.pop()
    if path[-1] % n == 0: fp = path[::-1]; break
fp, h = [i//n for i in fp], []
for i in range(len(fp)-1): h.append(fp[i] == fp[i+1] == 0 or fp[i] == fp[i+1] + 1)
ans, pos = [[]], 0
while pos < len(h):
    if h[pos] and len(ans[-1]) == 0: ans[-1].append(pos)
    elif not h[pos] and len(ans[-1]) == 1: ans[-1].append(pos); ans.append([])
    pos += 1
if len(ans[-1]) == 1: ans[-1].append(pos)
if not ans[-1]: ans.pop()
print(len(ans)), [print(a, b-a) for a, b in ans]