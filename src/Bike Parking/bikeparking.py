import sys; input = sys.stdin.readline; from collections import deque
n = int(input()); z = 0; ok = 1
a = deque([i, e] for i, e in enumerate(map(int, input().split())) if e)
b = deque([i, e] for i, e in enumerate(map(int, input().split())) if e)
while ok:
    c = deque(); d = deque(); ok = 0
    for _ in range(len(b)):
        q = b.popleft()
        while a and a[0][0] < q[0]: c.append(a.popleft())
        while q[1] and c:
            u = min(q[1], c[-1][1]); ok = 1
            z += u; q[1] -= u; c[-1][1] -= u
            if c[-1][1] == 0: c.pop()
        if q[1]: d.append(q)
    a, b = c+a, d
ok = 1
while ok:
    c = deque(); d = deque(); ok = 0
    for _ in range(len(b)):
        q = b.popleft()
        while a and a[0][0] <= q[0]: c.append(a.popleft())
        while q[1] and c:
            u = min(q[1], c[-1][1]); ok = 1
            q[1] -= u; c[-1][1] -= u
            if c[-1][1] == 0: c.pop()
        if q[1]: d.append(q)
    a, b = c+a, d
print(z-sum(e for i,e in b))