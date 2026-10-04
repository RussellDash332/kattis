import sys; input = sys.stdin.readline
n, m = map(int, input().split())
c = [*map(int, input().split()), 0]
u = [0]*-~n
for _ in range(m): s, e = map(int, input().split()); u[e-1] = max(u[e-1], s)
k = 0; N = n+2; D = [10**18]*2*N
def update(i, x):
    i += N; D[i] = x
    while i > 1: i >>= 1; D[i] = min(D[i<<1], D[(i<<1)+1])
def query(i, j):
    i += N; j += N; x = 10**18
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = min(x, D[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = min(x, D[j-1]); j >>= 1
    return x
update(0, 0)
for i in range(1, n+2): update(i, c[i-1]+query(k, i)); k = max(k, u[i-1])
print(D[N-1])