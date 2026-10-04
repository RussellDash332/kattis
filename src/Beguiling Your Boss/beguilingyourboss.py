import sys; input = sys.stdin.readline; from collections import *
N, K = map(int, input().split()); A = [*range(K+1)]; H = 0; M = 9223372036737335297
for i in range(K+1): H = (67*H+A[i])%M
Z = [H]; S = [1]
for i in range(K): S += [S[-1]*67%M]
for _ in range(N): a, b = map(int, input().split()); H = (H+(A[b]-A[a])*(S[K-a]-S[K-b]))%M; A[a], A[b] = A[b], A[a]; Z += [H]
print(sum(i*~-i for i in Counter(Z).values())//2)