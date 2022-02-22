from heapq import *
from collections import deque
import sys

c, n, a = list(map(int, input().split()))
arr = []
times = {}

for line in sys.stdin:
    arr.append(int(line))

for i in range(a):
    if arr[i] not in times:
        times[arr[i]] = deque([i])
    else:
        times[arr[i]].append(i)

used, ans = 0, 0
active = [False] * n
pq = [] # max PQ of times for the next read
for i in range(a):
    if not active[arr[i]]:
        active[arr[i]] = True
        ans += 1
        if used < c:
            used += 1
        else: # need to evict something
            _, id_evict = heappop(pq) # pop the cache that is going to be met gain next latest
            active[id_evict] = False
    times[arr[i]].popleft() # this must be i but we need the next timings to compare in the PQ
    if times[arr[i]]:
        heappush(pq, (-times[arr[i]][0], arr[i]))
    else:
        heappush(pq, (-a, arr[i]))
print(ans)