from heapq import *
n = int(input())
arr = list(map(int, input().split()))
s = list(range(1, n-1)) + list(range(2, n))
s.sort()
lim = n - 2
t, h = [], []
while len(t) != n - 2:
    if s and s[-1] >= lim:
        heappush(h, arr[s.pop()])
        continue
    lim -= 1
    t.append(heappop(h))
print(sum(t) + arr[-1])