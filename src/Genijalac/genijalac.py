from math import *
N, A, B, C, D, *P = map(int, open(0).read().split()); E = [0]*N; c = 0; V = [0]
for i in range(N):
    if E[i] == 0:
        c += 1; E[i] = c; p = P[i]-1; s = 1
        while E[p] == 0: E[p] = c; p = P[p]-1; s += 1
        V.append(s)
L = lcm(*(V[E[i]] for i in range(C, N-D))); print((B-1)//L-(A-2)//L)