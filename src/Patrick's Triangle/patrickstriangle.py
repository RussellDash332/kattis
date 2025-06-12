import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
F = array('I', [1]); I = array('I', [0]); M = 10**9+7
for i in range(10**6+1): F.append(F[-1]*(i+1)%M); I.append(pow(i+1, -1, M))
def f(N, K):
    if N < 4 or K == 1 or K == N: return N*(N+1)//2%M
    return F[N-1]*pow(F[K-2]*F[N-K-1], -1, M)*(N*(I[N-K]*I[N-K+1]*I[N-K+2]+I[K-1]*I[N-K]*I[N-K+1]+I[K-1]*I[K]*I[N-K]+I[K-1]*I[K]*I[K+1])-I[K-1]*I[N-K])%M
for _ in range(int(input())): N, K, X = map(int, input().split()); sys.stdout.write(['Inc','C'][f(N, K)==X]+'orrect\n')