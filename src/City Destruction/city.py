import sys; input = sys.stdin.readline; sys.setrecursionlimit(10000)
for _ in range(int(input())):
    N, D = map(int, input().split()); H = [*map(int, input().split())]; E = [*map(int, input().split()), 0]; M = [-1]*2*N
    def dp(i, l, e):
        if i == N: return 0
        if M[2*i+l] != -1: return M[2*i+l]
        M[2*i+l] = min(dp(i+1, 1, E[i])+max((H[i]-e+D-1)//D, 0), dp(i+1, 0, 0)+max((H[i]-e+D-1-E[i+1])//D, 0)); return M[2*i+l]
    print(dp(0, 0, 0))