from heapq import *; import sys; input = sys.stdin.readline
N, M, P = map(int, input().split()); M = {}
for _ in range(N): n, *x = input().split(); M[n] = [*map(int, x)]; heapify(M[n])
while M:
    n, v = min(M.items(), key=lambda x: (x[1][0], x[0])); heappop(M[n])
    for m in M:
        if M[m] and m != n: k = heappop(M[m]); heappush(M[m], k+P)
    if not M[n]: print(n); del M[n]