import sys; input = sys.stdin.readline; from heapq import *; from array import *
N = int(input()); Q = []; M = 2*10**9+1; L = 2*N+6; H = {}; D = array('i', [0]*L); C = array('i', [0]*L); F = B = N+3
for _ in range(N):
    s, *v = input().split(); x = int(v[0])
    if s[4] == 'T':
        if (y:=int(v[1])) not in H: H[y] = 0
        H[y] += x; D[F-1] = y; C[F-1] = x; F -= 1; heappush(Q, -H[y]*M+y)
    elif s[4] == 'B':
        if (y:=int(v[1])) not in H: H[y] = 0
        H[y] += x; D[B] = y; C[B] = x; B += 1; heappush(Q, -H[y]*M+y)
    elif s[7] == 'T':
        while x: u = min(C[F], x); x -= u; C[F] -= u; H[z:=D[F]] -= u; F += C[F] < 1; heappush(Q, -H[z]*M+z)
    else:
        while x: u = min(C[B-1], x); x -= u; C[B-1] -= u; H[z:=D[B-1]] -= u; B -= C[B-1] < 1; heappush(Q, -H[z]*M+z)
    while -(Q[0]//M) != H[Q[0]%M]: heappop(Q)
    sys.stdout.write(str(Q[0]%M)+'\n')