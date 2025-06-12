C, n1, n5, n10 = map(int, input().split()); M = {}
def f(C, n1, n5, n10):
    if C == 0: return 0
    K = 501*(151*(101*n10+n5)+C)+n1
    if K in M: return M[K]
    z = 10**9
    if n10:             z = min(z, f(C-1, n1+2, n5, n10-1)+1)
    if n5>1:            z = min(z, f(C-1, n1+2, n5-2, n10)+2)
    if n10 and n1>2:    z = min(z, f(C-1, n1-3, n5+1, n10-1)+4)
    if n5 and n1>2:     z = min(z, f(C-1, n1-3, n5-1, n10)+4)
    if n1>7:            z = min(z, f(C-1, n1-8, n5, n10)+8)
    M[K] = z; return z
print(f(C, n1, n5, n10))