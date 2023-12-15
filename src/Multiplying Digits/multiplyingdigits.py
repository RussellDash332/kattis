from collections import *
b, n = map(int, input().split()); m = {i:i for i in range(1, b) if n%i==0}; q = deque(m); INF = 1<<64
while q:
    u = q.popleft(); v = m[u]; w = n//u
    for d in range(v%b, b):
        if w%d == 0:
            if (k:=d*u) not in m: m[k] = INF; q.append(k)
            m[k] = min(m[k], b*v+d)
print(m.get(n, 'impossible'))