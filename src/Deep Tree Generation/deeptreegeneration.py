from collections import *
N, *P = map(int, open(0).read().split()); C = Counter(P); S = sorted(C); Z = [-1]*N; p = 0
for i in range(len(S)-1): Z[S[i+1]-1] = S[i]; C[S[i]] -= 1
for i in range(1, N):
    if Z[i] == -1:
        while C[S[p]] == 0: p += 1
        Z[i] = S[p]; C[S[p]] -= 1
print(*Z[1:])