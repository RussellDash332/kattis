import sys; sys.set_int_max_str_digits(K:=50001)
A, B = input().split(); A = str(int(A)-1).zfill(K+1); B = B.zfill(K+1); M = 10**9+7
def f(L, R):
    V = [[(0, 0)]*4 for _ in range(K+2)]; V[-1] = [(0, 1)]*4
    for p in range(K, -1, -1):
        for tl in (0, 1):
            for tr in (0, 1):
                s = t = 0
                for x in range(10 if tl else int(L[p])+1):
                    for y in range(10 if tr else int(R[p])+1): a, b = V[p+1][2*(tl|(x!=int(L[p])))+(tr|(y!=int(R[p])))]; s += abs(x-y)*b+a; t += b
                V[p][2*tl+tr] = s%M, t%M
    return V[0][0][0]
print((f(B, B)-f(B, A)-f(A, B)+f(A, A))%M)