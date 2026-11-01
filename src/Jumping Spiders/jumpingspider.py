R, C = map(int, input().split())
M = [[*map(int, input().split())] for _ in range(R)]
A = [[0]*C for _ in range(R)]
B = [[0]*C for _ in range(R)]
G = [[] for _ in range(R*C)]
for i in range(R):
    for j in range(C): A[i][j] = sum(M[i+p][j+q] for p in range(-3, 4) for q in range(-3, 4) if R>i+p>-1<j+q<C>0<abs(p)+abs(q)<4)>=7 and M[i][j]
for i in range(R):
    for j in range(C): B[i][j] = any(A[i+p][j+q] for p in range(-3, 4) for q in range(-3, 4) if R>i+p>-1<j+q<C>0<abs(p)+abs(q)<4)*M[i][j]
for i in range(R):
    for j in range(C):
        for p in range(-3, 4):
            for q in range(-3, 4):
                if R>i+p>-1<j+q<C>0<abs(p)+abs(q)<4 and A[i][j]|B[i][j] and A[i+p][j+q]|B[i+p][j+q]: G[i*C+j] += [i*C+j+p*C+q]; G[i*C+j+p*C+q] += [i*C+j]
V = [0]*R*C; H = []; Z = 0
for i in range(R*C):
    if V[i]<1:
        V[i] = 1; Q = [i]; h = 0
        for u in Q:
            h |= A[u//C][u%C]; Z += M[u//C][u%C]
            for v in G[u]:
                if V[v]<1: V[v] = 1; Q += [v]
        if h: H += [len(Q)]
print('YNeos'[not H::2])
print(max(len(H)-1, 0))
print(Z-sum(H))