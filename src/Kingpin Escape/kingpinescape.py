import sys; input = sys.stdin.readline
n, x = map(int, input().split()); g = [[] for _ in range(n)]; s = [(x, -1)]; m = []
for _ in range(n-1): a, b = map(int, input().split()); g[a].append(b); g[b].append(a)
while s:
    u, p = s.pop()
    for v in g[u]:
        if v != p: s.append((v, u))
    if len(g[u]) == 1: m.append(u)
print((len(m)+1)//2); y = len(m)//2
for i in range((len(m)+1)//2): print(m[i], m[(i+y)%len(m)])