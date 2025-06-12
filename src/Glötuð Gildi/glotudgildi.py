from math import *
N, *A = map(int, open(0).read().split()); H = {}; A.sort()
if any(sum(A[:i+1])<i*(i+1)//2 for i in range(N-1)) or sum(A)!=N*(N-1)//2: print(0); exit()
B = [[comb(n, k) for k in range(n+1)] for n in range(N+1)]
def dp(A):
    while A and A[-1] == len(A)-1: A.pop()
    if not A: return 1
    if A[0] < 0 or A[-1] >= len(A): return 0
    if A[-1] > len(A)-1: return 0
    if (K:=tuple(A)) in H: return H[K]
    # A[-1] must lose for L = len(A)-1-A[-1] times
    # Find all sequences if we decrement any element from A[:-1] for L times
    # e.g. [1, 2, 2, 2]+[3] means L = 1, so it can be [0, 2, 2, 2] (1x) or [1, 1, 2, 2] (3x)
    L = len(A)-1-A[-1]; A.pop(); F = [0]*(max(A)+1)
    for i in A: F[i] += 1
    def bt(f=[0]*len(F), l=0, idx=0):
        if idx == len(F):
            if l != L: return 0
            c = 1; a = []
            for i in range(len(F)): c *= B[F[i]][f[i]]; a.extend([i]*(F[i]-f[i]+(f[i+1] if i < len(F)-1 else 0)))
            return c*dp(a)
        Z = 0
        for i in range(F[idx]+1): Z += bt(f, l, idx+1); f[idx] += 1; l += 1
        f[idx] = 0
        return Z
    H[K] = bt(); return H[K]
print(dp(A))