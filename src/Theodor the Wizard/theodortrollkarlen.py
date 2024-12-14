M = 10**9+7; N, K, S, A = map(int, input().split()); F = [1]; J = [1]
for i in range(max(N, K)): F.append(F[-1]*(i+1)%M); J.append(J[-1]*S%M)
I = [pow(f, -1, M) for f in F]
Z = lambda k: sum(F[N]*I[N-i]*I[i]*pow(A*k, N-i, M)*F[k]*I[k-i]*I[i]*J[i] for i in range(min(N, k)+1))
print((Z(K)-Z(K-1))%M)