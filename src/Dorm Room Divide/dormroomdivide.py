def area(p):
    a, n = 0, len(p)
    for i in range(n): a += p[i][0]*p[(i+1)%n][1] - p[i][1]*p[(i+1)%n][0]
    return abs(a)/2
N = int(input())
P = [[*map(int, input().split())] for _ in range(N)]
A = [area((P[0], P[i], P[i+1])) for i in range(1, N-1)]
Z = sum(A)
U = 0
for i in range(1, N-1):
    if 2*(U+A[i-1]) <= Z: U += A[i-1]
    else:
        t = 1-(Z/2-U)/A[i-1]
        x = t*P[i][0]+(1-t)*P[i+1][0]
        y = t*P[i][1]+(1-t)*P[i+1][1]
        print(x, y), exit(0)