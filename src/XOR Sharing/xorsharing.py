N, *A = map(int, open(0).read().split())
B = [0]*30; I = [0]*30; Z = L = z = 0
for r in range(N):
    x = A[r]; ii = mi = r+1; d = 1
    if x == 0:
        if z: L = max(L, z)
        z = r+1
    else:
        for i in range(29, -1, -1):
            if (x>>i)&1:
                if B[i]<1: B[i] = x; I[i] = ii; d = 0; break
                if I[i]<ii: x, B[i] = B[i], x; ii, I[i] = I[i], ii
                mi = min(mi, ii, I[i]); x ^= B[i]
        if d: L = max(L, mi)
    Z += L
print(Z)