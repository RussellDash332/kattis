import sys; input = sys.stdin.readline; from functools import *
N = int(input()); G = [[] for _ in range(N)]; A = []; B = []
for _ in range(N): a, b = map(int, input().split()); A += [a]; B += [b]
for _ in range(N-1): a, b = map(int, input().split()); G[a] += [b]; G[b] += [a]
M = max(A)
@cache
def v(n, f=-1, d=0):
    if d*d > M: return 0
    if ~f: return v(n, d=d)-v(f, n, d+1)
    return A[n]//(B[n]+d*d) + sum(v(k, n, d+1) for k in G[n])
print(max(range(N), key=v))