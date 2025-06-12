n, K = map(int, input().split()); P = [[*map(int, input().split())] for _ in range(n)]; T = min(int(input()), 10**5); D = [-10**13]*(T+1)*(n+1); D[T] = 0; p = T+1; q = 0
for i in range(n):
    a, b = P[i]
    for k in range(T+1):
        if k>=a and D[p-a] < D[q]+b: D[p-a] = D[q]+b
        if k>=K and D[p-K] < D[q]: D[p-K] = D[q]
        p += 1; q += 1
print(max(D))