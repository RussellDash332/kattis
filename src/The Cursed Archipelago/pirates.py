def rref(A):
    N, M = len(A), len(A[0])
    def equal(a, b): return a==b
    def lead(A, r):
        row = A[r]; i = 0
        while i < M and equal(row[i], 0): i += 1
        return i
    def allpv(A):
        p = []
        for r in range(N):
            k = lead(A, r)
            if k != M: p.append((r, k))
        return sorted(p, reverse=1)
    def col(A, i): return [*map(lambda x: x[i], A)]
    def ero(A, i, j, c):
        for k in range(M): v = A[i][k]+c*A[j][k]; A[i][k] = v%MOD
    cc = cr = 0
    while cc < M and cr < N:
        if equal(A[cr][cc], 0):
            kc = col(A, cc)[cr+1:]
            for i in range(len(kc)):
                if not equal(kc[i], 0): break
                elif i == len(kc)-1: i += 1
            if i < len(kc): A[cr], A[cr+i+1] = A[cr+i+1], A[cr]
            else: cc += 1
        else:
            if not equal(A[cr][cc], 1):
                c = pow(A[cr][cc], -1, MOD)
                for j in range(M): v = A[cr][j]*c; A[cr][j] = v%MOD
            for i in range(cr+1, N):
                if not equal(A[i][cc], 0): ero(A, i, cr, -A[i][cc])
            cc += 1; cr += 1
    pv = allpv(A)
    for i in range(len(pv)-1):
        for j in range(pv[i][0]-1, -1, -1): ero(A, j, pv[i][0], -A[j][pv[i][1]])
    return A

def berlekamp_massey(S):
    C = [1]; B = [1]; L = 0; m = b = 1
    for n, s in enumerate(S):
        if (d:=(s+sum(C[i]*S[n-i] for i in range(1, L+1)))%MOD):
            T = C[:]; c = d*pow(b, -1, MOD)%MOD; C.extend([0]*(len(B)+m-len(C)))
            for i in range(len(B)): C[i+m] = (C[i+m]-c*B[i])%MOD
            if 2*L > n: m += 1
            else: L = n+1-L; B = T; b = d; m = 1
        else: m += 1
    return [-x%MOD for x in C[1:]]

def berlekamp_welch(T, Y, K, L):
    Q = len(T); mat = []
    for q in range(Q):
        tq = T[q]; yq = Y[q]; row = []; tp = 1
        for j in range(K+L): row.append(tp); tp = tp*tq%MOD
        tp = 1
        for j in range(L): row.append(-yq*tp%MOD); tp = tp*tq%MOD
        row.append(yq*tp%MOD); mat.append(row)
    rref(mat)
    if L == 0: return [mat[j][-1] for j in range(K)]
    nv = K+2*L; S = [0]*nv
    for r in range(len(mat)):
        c = 0
        while c < nv and mat[r][c] < 1: c += 1
        if c < nv: S[c] = mat[r][-1]
    # long division N/E
    Nx = S[:K+L]; np = len(Px:=Nx[:])-1; nq = len(Ex:=S[K+L:]+[1])-1; Qx = [0]*(np-nq+1)
    for i in range(np-nq, -1, -1):
        c = Px[i+nq]*pow(Ex[nq], -1, MOD)%MOD; Qx[i] = c
        for j in range(nq+1): Px[i+j] = (Px[i+j]-c*Ex[j])%MOD
    return Qx

N, Z, L, Q, MOD = map(int, input().split()); K = 2*Z
IK = [pow(i, K, MOD) for i in range(N+1)]
T = [*range(1, Q+1)]; Y = []

# geometric series sum of S_q
for q in range(Q):
    tq = T[q]; tk = pow(tq, K, MOD); A = [0]*N; zi = -1; P = [1]*-~N; X = [0]*N
    for i in range(N):
        d = (-~i*tq-1)%MOD
        if d: A[i] = d
        else: zi = i; A[i] = 1
    for i in range(N): P[i+1] = P[i]*A[i]%MOD
    J = pow(P[N], -1, MOD); I = [0]*N
    for i in range(N-1, -1, -1): I[i] = P[i]*J%MOD; J = J*A[i]%MOD
    for i in range(1, N+1):
        if i-1 == zi: X[i-1] = K
        else: X[i-1] = (IK[i]*tk-1)*I[i-1]%MOD
    print('?', *X); Y.append(int(input()))

S = berlekamp_welch(T, Y, K, L)
R = berlekamp_massey(S)
zL = len(R)

G = []
# polynomial evaluation P(z_i) = 0
for i in range(1, N+1):
    v = 1
    for c in R: v = (v*i-c)%MOD
    if v == 0: G += [i]

# finalize
nZ = len(G); zX = [0]*-~N
if nZ:
    v_mat = [[pow(i, k, MOD) for i in G]+[S[k]] for k in range(nZ)]; rref(v_mat)
    for i, x in enumerate(G): zX[x] = v_mat[i][-1]
print('!', nZ)
for i in G: print(i, zX[i])