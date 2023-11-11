a, b = map(int, input().split()); m = 10**9+7; n = int(input())
if n == 0: print(a, b), exit(0)
def matpow(mat, n):
    if n == 1: return mat
    elif n % 2:
        (a, b), (c, d) = mat; (a2, b2), (c2, d2) = matpow(mat, n-1)
        return (((a*a2+b*c2)%m, (a*b2+b*d2)%m), ((c*a2+d*c2)%m, (c*b2+d*d2)%m))
    (a, b), (c, d) = mat; return matpow((((a*a+b*c)%m, b*(a+d)%m), (c*(a+d)%m, (b*c+d*d)%m)), n//2)
(p, q), (r, s) = matpow([[1, 1], [1, 2]], n); print((a*p+b*q)%m, (a*r+b*s)%m)