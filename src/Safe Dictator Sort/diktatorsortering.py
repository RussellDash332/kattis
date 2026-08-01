from bisect import *
N, *A = map(int, open(0).read().split())
B = []
for e in A:
    p = bisect(B, -e, key=lambda x:-x[-1])
    if p == len(B): B.append([e])
    else: B[p] += [e]
for b in B: print(*b)