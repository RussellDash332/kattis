from array import *
N, X, Y = map(int, input().split()); K = min(N//X, N//Y); M = 10**9+7; F = array('i', [1, 1])
for i in range(N): F.append(F[-1]*(i+2)%M)
I = array('i', [pow(i, -1, M) for i in F]); S = 0
for k in range(K): S += F[N-k*X+k-X]*I[N-k*X-X]%M*F[N-k*Y+k-Y]*I[N-k*Y-Y]*I[k]**2%M; S %= M
print(S)