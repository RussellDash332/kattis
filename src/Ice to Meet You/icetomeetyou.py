import sys; input = sys.stdin.readline
N = int(input()); P = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = P[i]; x2, y2 = P[j]
        a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1; V = {}
        for k in range(N):
            if k == i or k == j: continue
            x, y = P[k]; v = a*x+b*y
            if v not in V: V[v] = []
            V[v].append(k)
        if c not in V: print(i+1, j+1); exit()
        if len(V) == 1: print('learning is guaranteed!'); exit()