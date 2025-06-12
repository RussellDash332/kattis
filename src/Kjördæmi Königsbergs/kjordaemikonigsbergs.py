# Takes in a degree sequence D, returns an edge list E with degree sequence D
def havel_hakimi(D):
    E = []; Q = [[] for _ in range(max(D)+1)]; L = 1; R = len(Q)-1; T = []; J = array('i', (i-1 for i in range(R+1)))
    for i in range(len(D)): Q[D[i]].append(i)
    while L <= R:
        if not Q[L]: L += 1; continue
        v = Q[L].pop(); S = R; B = []
        for _ in range(L):
            while S and not Q[S]: B.append(S); S = J[S]
            if S < 1: return
            u = Q[S].pop(); E.append((u, v))
            if S > 1: T.append((u, S-1))
        while T:
            u, x = T.pop()
            if J[x+1] != x: J[x], J[x+1] = J[x+1], x
            Q[x].append(u)
        for b in B:
            if not Q[J[b]]: J[b] = J[J[b]]
        L -= S==L
    return E
import sys, os, io; from array import *
N, *A = map(int, io.BytesIO(os.read(0, os.fstat(0).st_size)).read().split()); H = havel_hakimi(A)
if H == None or sum(A) < 2*N-2: print('Omogulegt!'); exit()
print(N, len(H))
for a, b in H: sys.stdout.write(f'{a+1} {b+1}\n')