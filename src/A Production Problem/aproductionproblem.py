def simplex(A, C):
    m, n = len(A), len(A[0])-1; c = [[0]*(m+n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n): c[i][j] = A[i][j]
        c[i][-1] = A[i][-1]
    for i in range(n): c[-1][i] = C[i]
    for i in range(m): c[i][i+n] = 1
    while True:
        if (col:=min([(i,e) for i,e in enumerate(c[-1]) if e<0], key=lambda x: x[1], default=[-1])[0]) == -1: break
        if (row:=min([(i,e,c[i][-1]/c[i][col]) for i,e in enumerate(c[t][col] for t in range(m)) if e>0], key=lambda x: x[2], default=[-1])[0]) == -1: break
        k = c[row][col]
        for i in range(m+n+1): c[row][i] /= k
        for i in range(m+1):
            if i == row: continue
            k = c[i][col]
            for j in range(m+n+1): c[i][j] -= k*c[row][j]
    return c[-1][-1]
m, n = map(int, input().split()); A = [[0]*(n+1) for _ in range(m)]; C = []
for i, e in enumerate(map(int, input().split())): A[i][n] = e
for i in range(n):
    *v, p = map(float, input().split()); C.append(-p)
    for j in range(m): A[j][i] = v[j]/100
print('%.2f'%simplex(A, C))