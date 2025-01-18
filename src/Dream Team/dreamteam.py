N, P, Q = map(int, input().split())
A = [*map(int, input().split())]
S = [*map(int, input().split())]
W = [[] for _ in range(100-P)]
M = 10**11
for i in range(100-P):
    for j in range(N):
        if i+1 <= A[j] <= i+1+P: W[i].append(S[j])
for w in W:
    w.sort()
    for i in range(len(w)-11):
        if w[i+11]-w[i] <= Q: M = min(M, sum(w[i:i+12]))
if M == 10**11: print('NO')
else: print('YES', M)