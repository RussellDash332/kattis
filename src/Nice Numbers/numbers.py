import sys; input = sys.stdin.readline
from collections import deque
for _ in range(int(input())):
    s = deque(map(int, [*input().strip()])); s2 = deque()
    if len(s) == 1: print(''.join(map(str, s))); continue
    q = []; q2 = []; q3 = []
    while s:
        u = s.popleft()
        if u == 2:
            q.append(22), s2.append(4)
            if s and s[0] == u: s.popleft()
        else: q.append(u), s2.append(u)
    q = deque(q)
    if len(s2) == 1: print(''.join(map(str, q))); continue
    while s2:
        u = s2.popleft(); ou = q.popleft()
        if u == 4:
            q.append(ou), q.append(q[0]), q2.append(44), q3.append(8)
            if s2 and s2[0] == u: s2.popleft(); q.popleft()
            else: q.pop(), q.append(4)
        else: q.append(ou), q2.append(u), q3.append(u)
    c = sum(q3); pad = [8]*(((1<<(len(bin(c-1))-2))-c)//8)
    print(''.join(map(str, [*q, *pad])))