import sys; input = sys.stdin.readline
N = int(input())
A = [*map(int, input().split())]
H = [0]*2*N; L = [10**18]*2*N
def update(i, x):
    i += N; H[i] = L[i] = x
    while i > 1: i >>= 1; H[i] = max(H[i<<1], H[(i<<1)+1]); L[i] = min(L[i<<1], L[(i<<1)+1])
def query(i, j):
    i += N; j += N; x = 0; y = 10**18
    while i < j:
        if i&1: x=max(x,H[i]); y=min(y,L[i]); i+=1
        if j&1: j-=1; x=max(x,H[j]); y=min(y,L[j])
        i >>= 1; j >>= 1
    return y, x
for i in range(N): update(i, A[i]*N+i)
Q, T = map(int, input().split())
for _ in range(Q):
    c, l, r = input().split(); l, r = query(int(l)-1, int(r))
    if c>'L': print(['DANGER', 'SAFE'][r//N-l//N<T])
    else: m, M = l//N, r//N; update(l%N, (m+M)//2*N+l%N); update(r%N, (m+M+1)//2*N+r%N)