import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from heapq import *
input(); a = sorted(zip(map(int, input().split()), map(int, input().split())), reverse=1); z = 0; q = []
for x in sorted(map(int, input().split())):
    while a and a[-1][0] <= x: heappush(q, a.pop()[1])
    while q and q[0] < x: heappop(q)
    if q: z += 1; heappop(q)
print(z)