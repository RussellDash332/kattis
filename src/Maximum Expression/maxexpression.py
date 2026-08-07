import sys; sys.setrecursionlimit(6767); from functools import *
from math import *
n = int(input())
B = []; N = []
for s in input().split('+'):
    t, *u = s.split('-')
    if t: B += [len(t.split('*'))]
    for v in u: N += [len(v.split('*'))]
n0, n1, n2 = map(int, input().split())
B.sort(reverse=1); N.sort(reverse=1)
C = [[] for _ in B]; M = [[] for _ in N]; Z = 0
if n0 < len(N):
    for i in range(len(B)):
        for _ in range(B[i]):
            if n2: C[i].append(2); n2 -= 1
            elif n1: C[i].append(1); n1 -= 1
    for i in range(len(N)):
        if n0:
            M[i].append(0); n0 -= 1
            for _ in range(N[i]-1):
                if n2: M[i].append(2); n2 -= 1
                elif n1: M[i].append(1); n1 -= 1
    z = [i for i in range(len(N)-1, -1, -1) if not M[i]]
    while 1:
        c = 0
        for i in z:
            if len(M[i]) < N[i] and n2: M[i].append(2); n2 -= 1; c = 1
        if c<1: break
    while 1:
        c = 0
        for i in z:
            if len(M[i]) < N[i] and n1: M[i].append(1); n1 -= 1; c = 1
        if c<1: break
    print(sum(map(prod, C))-sum(map(prod, M)))
else:
    S = sum(N); u = min(n0, S); n0 -= u; S -= u; u = min(n1, S); n1 -= u; S -= u; u = min(n2, S); n2 -= u; S -= u
    @cache
    def f(i, n0, n1, n2):
        if n0 < 0: return 0
        s = 0
        while i < len(B) and n2 >= B[i]: s += 1<<B[i]; n2 -= B[i]; i += 1
        if i == len(B): return s
        # at this point, found a bin of size B[i] and we can only partially fill with n2<B[i] twos
        r1 = B[i]-n2
        if n1 >= r1: v = 2**n2; r = n1-r1   # enough 1s to fill the rest?
        else: v = 0; r = n1                 # this bin will become 0, let's see if can handle the rest first
        for sz in sorted(B[i+1:]):
            if r >= sz: v += 1; r -= sz
        return s+max(v, f(i+1, n0-1, n1, n2))
    print(f(0, n0, n1, n2))