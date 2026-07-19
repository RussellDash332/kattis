import sys; input = sys.stdin.readline
N, M = map(int, input().split()); Q = []; A = [10**18]*2*N; S = 0
def update(l, r, x):
    l += N; r += N
    while l <= r:
        if l&1: A[l] = min(A[l], x)
        if r^1&1: A[r] = min(A[r], x)
        l = (l+1)>>1; r = (r-1)>>1
def query(i):
    i += N; z = 10**18
    while i > 0: z = min(z, A[i]); i >>= 1
    return z
for _ in range(M): l, r, c = map(int, input().split()); update(l, r-1, c)
for i in range(N): S += query(i); print(-1 if S>10**17 else S)