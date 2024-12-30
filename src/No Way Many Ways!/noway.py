import sys; input = sys.stdin.readline; M = 10**9+7
R, C, N = map(int, input().split()); W = [0]*(R+C-1)
for _ in range(N):
    r, m = map(int, input().split())
    for i in range((r+R-1)%m, R+C-1, m): W[i] = 1
D = [[0]*C for _ in range(R)]; D[0][0] = int(W[R-1]<1)
for i in range(R):
    for j in range(C):
        if W[j-i+R-1]: continue
        if i: D[i][j] += D[i-1][j]
        if j: D[i][j] += D[i][j-1]
        D[i][j] %= M
print(D[-1][-1])