import os, io
N, C, T, *A = map(int, io.BytesIO(os.read(0, os.fstat(0).st_size)).read().split()); B = []; p = 0; D = [0]*2*N
def update(i, x):
    i += N; D[i] = x
    while i > 1: i >>= 1; D[i] = max(D[i<<1], D[(i<<1)+1])
def query(i, j):
    i += N; j += N; x = 0
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = max(x, D[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = max(x, D[j-1]); j >>= 1
    return x
for i in range(N):
    while p < N and A[p] < A[i]+T: p += 1
    B.append(p-i)
for i in range(N-1, -1, -1): update(i, max(i, query(B[i]+i, min(B[i]+i+C, N))-B[i]+1))
print(query(0, 1))