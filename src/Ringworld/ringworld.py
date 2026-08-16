from heapq import *
for _ in range(int(input())):
    m, n = map(int, input().split()); I = []; N = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b: I += [(a, b+m)]; N += 1
        else: I += [(a, b), (a+m, b+m)]; N += 2
    if n > m: print('NO'); continue
    I.sort(); i = x = 0; Q = []
    while i < N or Q:
        if not Q: x = max(x, I[i][0])
        while i < N and I[i][0] <= x: heappush(Q, I[i][1]); i += 1
        if heappop(Q) < x: print('NO'); break
        x += 1
    else: print('YES')