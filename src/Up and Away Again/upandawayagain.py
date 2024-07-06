import sys; input = sys.stdin.readline; from array import *
N = 200001; n, x, t = map(int, input().split()); INF = 2*N; h = array('i', map(int, input().split())); d = array('i', map(int, input().split())); dp = array('i', [INF]*n); x -= 1; dp[x] = 0; T = array('i', [INF]*2*N)

# range update, point query
def update(l, r, x):
    while l <= r:
        if l&1: T[l] = min(T[l], x)
        if r^1&1: T[r] = min(T[r], x)
        l = (l+1)>>1; r = (r-1)>>1
def query(x):
    z = INF
    while x >= 1: z = min(z, T[x]); x >>= 1
    return z

update(N, h[x]+d[x]+N, 0)
for i in sorted(range(n), key=lambda x: h[x]):
    if h[i] >= h[x]:
        if i != x: dp[i] = min(dp[i], query(h[i]+N)+1)
        update(N, h[i]+d[i]+N, dp[i])
print(dp[0]*t if dp[0] != INF else -1)