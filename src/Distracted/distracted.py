from collections import deque
import sys

n, t = map(int, input().split())
st, m, v, visited, look = {}, [], 0, {}, {}

cnt = 0
for line in sys.stdin:
    line = line.strip()
    if cnt < n:
        a, b = line.split()
        st[a], visited[a] = b, False
        if b == 'm': m.append(a)
    else:
        a, d, b = line.split()
        look[a] = b
        if st[a] + st[b] in ['m?', '?u', '??']: v = '?'
    cnt += 1

# find m -> ... -> u
for i in m:
    if not visited[i]:
        visited[i], ptr, has_m = True, i, False
        while ptr in look and not visited[look[ptr]]:
            has_m |= (st[ptr] == 'm')
            ptr = look[ptr]
            visited[ptr] = True
            if st[ptr] == 'u' and has_m: v = 1
print(v)