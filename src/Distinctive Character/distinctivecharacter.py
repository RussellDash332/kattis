import sys
from collections import deque

n, k = map(int, input().split())
q = deque()
vis = [0]*(2**k)
for line in sys.stdin:
    b = int(line, 2)
    q.append((b, 0))
    vis[b] = 1
while q:
    u, d = q.popleft()
    for s in range(k):
        nxt = u ^ (1<<s)
        if not vis[nxt]:
            vis[nxt] = 1
            q.append((u ^ (1 << s), d+1))
    best = u
print(bin(best)[2:].zfill(k))