from fractions import *
n, *a = map(int, open(0).read().split())
A = [(Fraction(a[i]), i) for i in range(n)]; K = []
for _ in range(1001):
    A.sort(); z = 1
    if len(A) > 1:
        x = A.pop(0); y = A.pop(); m = (x[0]+y[0])/2; z &= x[0]==y[0]
        if x[0]-y[0]: K.append([y[1]+1, x[1]+1])
        A.extend(((m, x[1]), (m, y[1]))); A.sort()
    if z: break
if len({k[0] for k in A}) != 1: print(-1), exit(0)
print(len(K)); [print(*r) for r in K]