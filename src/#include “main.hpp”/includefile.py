import sys; input = sys.stdin.readline; from bisect import *; from array import *
N, k, Q = map(int, input().split()); M = [input().rstrip() for _ in range(N)]; C = array('i', [-1] + [i for i in range(N) if M[i] == '#include "main.hpp"']); c = len(C)-1; D = array('i', [C[i+1]-C[i]-1 for i in range(c)]); F = C[1] if c else N
if c > 1:
    L = 1
    while c**L < 1e18: L += 1
    P = [[] for _ in range(L)]; S = []
    for l in range(L):
        U = (N-c)*(c**l-1)//(c-1)+c**l; p = 0; S += [U]
        for i in range(c): p += D[i]; P[l] += [p]; p += U; P[l] += [p]
def f(x, k):
    if c == 0 or x < F*k: return M[x%F]
    if x < F*k+N: return M[x-F*k]
    if c == 1: return M[(x-F*k-N)%(N-F-1)+F+1]
    l = bisect_left(S, x)
    if k > l: x -= F*(k-l); k = l
    while True:
        if k == 0 or x < F: return M[x]
        b = bisect(P[k], x)
        if b == 2*c: return M[C[-1]+x-P[k][-1]+1]
        elif b%2: x -= P[k][b-1]; k -= 1; continue
        else: return M[C[b//2+1]+x-P[k][b]]
for _ in range(Q): sys.stdout.write(f(int(input())-1, k)+'\n')