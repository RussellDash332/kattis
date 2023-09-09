import sys; input = sys.stdin.readline
from array import *
N = int(input()); A = array('i', sorted(int(input()) for _ in range(N))); H = {}
for i in range(N-1):
    a = A[i]
    for j in range(i+1, N-1):
        if a == (b:=A[j]): continue
        if a+b not in H: H[a+b] = (a, b)
        elif type(H[a+b]) == tuple: H[a+b] = [H[a+b], (a, b)]
        else: H[a+b].append((a, b))
for i in range(N-1, -1, -1):
    d = A[i]
    for j in range(N):
        if (c:=A[j]) == d or d-c not in H: continue
        if type(H[d-c]) == tuple: h = [H[d-c]]
        else: h = H[d-c]
        for a, b in h:
            if a not in (c,d) and b not in (c,d): print(d), exit(0)
print('no solution')