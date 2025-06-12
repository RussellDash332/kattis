import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N = int(input()); C = [*map(int, input().split()), 0]; A = [10**9]*2*N; E = []
for _ in range(int(input())): s, t = map(int, input().split()); E.append((t-1)*N+s-1)
def query(i, j):
    i += N; j += N; x = 10**9
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = min(x, A[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = min(x, A[j-1]); j >>= 1
    return x
p = v = 0; E.sort()
for i in range(N):
    while p < len(E) and E[p]//N <= i: v = max(v, E[p]%N*N+E[p]//N); p += 1
    if v: A[i+N] = C[i]+query(v//N, v%N)
    else: A[i+N] = C[i]
    i += N
    while i > 1: i >>= 1; A[i] = min(A[i<<1], A[(i<<1)+1])
print(query(N-1, N))