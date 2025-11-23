from bisect import *
def lis(A):
    B = []
    for e in A:
        p = bisect(B, e-1)
        if p == len(B): B.append(e)
        else: B[p] = e
    return len(B)
n, *x = map(int, open(0).read().split())
print(max(lis(x), lis([-i for i in x])))