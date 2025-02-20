from heapq import *
def rref(A):
    def equal(a, b): return a == b
    def leading_entry_col(A, r):
        row = A[r]; i = 0
        while i < len(A[0]) and equal(row[i], 0): i += 1
        return i
    def list_pivots(A):
        res = []
        for r in range(len(A)):
            k = leading_entry_col(A, r)
            if k != len(A[0]): res.append((r, k))
        return sorted(res, reverse=True)
    def col(A, i): return list(map(lambda x: x[i], A))
    def ero1(A, i, c):
        for j in range(len(A[0])): A[i][j] *= c; A[i][j] %= 13
    def ero2(A, i, j, c):
        for k in range(len(A[0])): A[i][k] += c*A[j][k]; A[i][k] %= 13
    def ero3(A, i, j): A[i], A[j] = A[j], A[i]
    curr_col = 0
    curr_row = 0
    while curr_col < len(A[0]) and curr_row < len(A):
        if equal(A[curr_row][curr_col], 0):
            check_col = col(A, curr_col)[curr_row+1:]
            for i in range(len(check_col)):
                if not equal(check_col[i], 0): break
                elif i == len(check_col)-1: i += 1
            if i < len(check_col): ero3(A, curr_row, curr_row+i+1)
            else: curr_col += 1
        else:
            if not equal(A[curr_row][curr_col], 1): ero1(A, curr_row, pow(A[curr_row][curr_col], -1, 13))
            for i in range(curr_row+1, len(A)):
                if not equal(A[i][curr_col], 0): ero2(A, i, curr_row, -A[i][curr_col])
            curr_col += 1
            curr_row += 1
    pivots = list_pivots(A)
    for i in range(len(pivots)-1):
        for j in range(pivots[i][0]-1, -1, -1): ero2(A, j, pivots[i][0], -A[j][pivots[i][1]])
    return A
N, A, R, T = map(int, input().split()); M = [201*[0] for _ in range(T)]; H = {}; C = 0
for i in range(T):
    d, p, *a = map(int, input().split()); M[i][-1] = d
    for j in range(p-1):
        t = (a[j]-1, a[j+1]-1)
        if t not in H: H[t] = H[t[::-1]] = C; C += 1
        M[i][H[t]] += 1; M[i][H[t]] %= 13
INF = float('inf'); M = rref(M); Z = 200*[INF]
for i in range(T):
    for j in range(200):
        if M[i][j] == 1: Z[j] = M[i][-1]
G = [{} for _ in range(N)]; D = [INF]*N; D[A-1] = 0; pq = [(0, A-1)]
for i in range(N):
    for j in range(i):
        if (i, j) not in H: continue
        if Z[H[(i, j)]] != INF: G[i][j] = G[j][i] = Z[H[(i, j)]]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn in G[vv]:
        if D[nn] > (new:=dd+G[vv][nn]): D[nn] = new; heappush(pq, (new, nn))
print(D[R-1])