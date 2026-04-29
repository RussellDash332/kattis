import sys; input = sys.stdin.readline
N, Q = map(int, input().split())
A = [0]*2*N
def update(i, x):
    i += N; A[i] = x
    while i > 1: i >>= 1; A[i] = min(A[i<<1], A[(i<<1)+1])
def query(i, j):
    i += N; j += N; x = 10**9
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = min(x, A[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = min(x, A[j-1]); j >>= 1
    return x
for _ in range(Q):
    c, k, v = input().split(); k = int(k)-1; v = int(v)
    if c < 'U': print(query(k, v))
    else: update(k, v)