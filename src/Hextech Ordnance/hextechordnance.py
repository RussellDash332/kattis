import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
N = int(input()); A = array('I', map(int, input().split())); S = 0; V = set(); B = [[] for _ in range(N+1)]; d = 0
for i in range(N-1):
    a = min(A[i], A[i+1]); b = max(A[i], A[i+1])
    if b-a <= N: V.add(i*N+i+1); B[b-a].append((i*N+i+1, a))
for S in range(1, N+1):
    while d <= N and not B[d]: d += 1
    if d > S: print('unstable'); exit()
    ij, a = B[d].pop()
    if ij > N and ij-N not in V:
        V.add(ij-N); a2 = min(a, v:=A[ij//N-1]); b2 = max(d+a, v)
        if b2-a2 <= N: B[b2-a2].append((ij-N, a2))
    if ij%N < N-1 and ij+1 not in V:
        V.add(ij+1); a2 = min(a, v:=A[ij%N+1]); b2 = max(d+a, v)
        if b2-a2 <= N: B[b2-a2].append((ij+1, a2))
print('stable')