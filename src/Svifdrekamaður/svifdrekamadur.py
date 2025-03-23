N, *a = map(int, open(0).read().split())
def nge(a):
    z = [0]*len(a); s = []
    for i in range(len(a)):
        while s and s[-1][1] < a[i]: k = s.pop()[0]; z[k] = i-k
        s.append((i, a[i]))
    return z
def update(i, x):
    i += N; A[i] = x
    while i > 1: i >>= 1; A[i] = max(A[i<<1], A[(i<<1)+1])
def query(i, j):
    i += N; j += N; x = 0
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = max(x, A[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = max(x, A[j-1]); j >>= 1
    return x
Z = 0
for _ in range(2):
    A = [0]*2*N
    for i in range(N): update(i, a[i])
    K = nge(a)
    for i in range(N):
        if K[i] < 2 or query(i+1, i+K[i]) < a[i]: Z = max(Z, K[i])
    a = a[::-1]
print(Z)