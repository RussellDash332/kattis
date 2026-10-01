def mul(a, b):
    c = [[0]*N for _ in range(N)]
    for i, ci in enumerate(c):
        for j, ax in enumerate(a[i]):
            for k, by in enumerate(b[j]): ci[k] += ax*by
    return c
r, c, n = map(int, input().split()); p = float(input()); R = [*range(N:=r*c)]
for _ in range(n): s, e = map(int, input().split()); R[s-1] = e-1
A = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(1, 7): A[i][R[min(N-1, i+j)]] += 1/6
A[-1][-1] = 1; P = [A]; z = 1; v = [1]+[0]*~-N
for _ in '.'*26: P += [mul(P[-1], P[-1])]
for i in range(26, -1, -1):
    q = P[i]; w = [0]*N
    for j, x in enumerate(v):
        for k, y in enumerate(q[j]): w[k] += x*y
    if w[-1] < p-1e-9: v = w; z += 1<<i
print(z)