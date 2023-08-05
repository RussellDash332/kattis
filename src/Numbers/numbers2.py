'''
Consider u_n = (3+sqrt(5))^n + (3-sqrt(5))^n
Then u_0 = 2, u_1 = 6, and u_(n+2) = 6u_(n+1) - 4u_n
Suffices to compute (u_n - 1)%1000 since 0 < (3-sqrt(5))^n < 1 for n > 1
Using the transition matrix ((0, 1), (-4, 6)), each query can be computed in O(log n) time!
'''
def matpow(mat, n):
    if n == 1: return mat
    elif n % 2:
        (a, b), (c, d) = mat
        (a2, b2), (c2, d2) = matpow(mat, n-1)
        return (((a*a2+b*c2)%1000, (a*b2+b*d2)%1000), ((c*a2+d*c2)%1000, (c*b2+d*d2)%1000))
    (a, b), (c, d) = mat; return matpow((((a*a+b*c)%1000, b*(a+d)%1000), (c*(a+d)%1000, (b*c+d*d)%1000)), n//2)
m = ((0, 1), (-4, 6))
for t in range(int(input())):
    a, b = matpow(m, int(input()))[0]
    print(f'Case #{t+1}:', str((2*a+6*b-1)%1000).zfill(3))