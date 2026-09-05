N, *A = map(int, open(0).read().split())
from bisect import *
def lis(A):
    B = []
    for e in A:
        p = bisect(B, e)
        if p == len(B): B.append(e)
        else: B[p] = e
    return len(B)
B = []
for i, e in enumerate(A):
    if e>=i+1: B += [(2*i+1, 2*(~i+e))]
    if e>=N-i: B += [(2*(e-N+i), 2*(N-i)-1)]
print(N-lis([x[1] for x in sorted(B)]))