import sys; input = sys.stdin.readline
N, K = map(int, input().split()); U, D = [0]*N, [0]*N; L = N; H = 0
for _ in range(K): b, p = map(int, input().split()); (U, D)[b-1][p:=p-1] = 1; L = min(L, p); H = max(H, p)
if K == 0: U[0] = 1; L = H = 0
for i in range(L-1, -1, -1): (D, U)[(L-i)%2-U[L]][i] = 1
for i in range(H+1, N): (D, U)[(H-i)%2-U[H]][i] = 1
for i in range(L+1, H):
    if U[i] or D[i]: continue
    if U[i-1] and not D[i+1]: D[i] = 1
    if D[i-1] and not U[i+1]: U[i] = 1
print(sum(U)+sum(D))
print(''.join('.X'[u] for u in U))
print(''.join('.X'[d] for d in D))