def twarea(p):
    a = 0
    for i in range(n): a += p[i][0]*p[(i+1)%n][1]-p[i][1]*p[(i+1)%n][0]
    return abs(a)
a, n = map(eval, input().split())
P = [[*map(int, input().split())] for _ in range(n)]
Q = [(P[i][0]+P[i-1][0], P[i][1]+P[i-1][1]) for i in range(n)]
Z = 4*twarea(P); print(2*((Z-twarea(Q))/Z/(1-a))**.5)