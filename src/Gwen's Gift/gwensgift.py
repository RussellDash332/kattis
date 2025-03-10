n, k = map(int, input().split()); F = [1]; k -= 1
for i in range(1, 21): F.append(F[-1]*i)
S = [1]*(n-1); P = [*range(1, n)]; V = [0]
for i in range(max(n-22, 0)): V.append(V[-1]+S[i])
for i in range(max(n-22, 0), n-1):
    S[i] = P[k//F[n-2-i]]; k %= F[n-2-i]
    V.append(V[-1]+S[i]); T = set()
    for q in range(len(V)): T.add((V[q]-V[-1])%n)
    P = [j for j in range(1, n) if j not in T]
print(*S)