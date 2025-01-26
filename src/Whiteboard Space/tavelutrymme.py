from array import *
N, R, C, *A = map(int, open(0).read().split()); Z = R*C+1; A = array('h', A); P = array('h', [-1]*Z*Z); S = [0]
for i in range(N):
    T = array('i')
    for rb in S:
        r, b = divmod(rb, Z)
        bb = b
        if r%C+A[i] < C: rr = r+A[i]
        elif r%C+A[i] > C: rr = r//C*C+C+A[i]
        else: rr = r//C*C+C
        if rr > bb: rr, bb = bb, rr
        if bb < Z and P[u:=rr*Z+bb] < i: P[u] = i; T.append(u)
        rr = r
        if b%C+A[i] < C: bb = b+A[i]
        elif b%C+A[i] > C: bb = b//C*C+C+A[i]
        else: bb = b//C*C+C
        if rr > bb: rr, bb = bb, rr
        if bb < Z and P[u:=rr*Z+bb] < i: P[u] = i; T.append(u)
    S = T
print(max(P)+1)