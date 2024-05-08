import sys; input = sys.stdin.readline
V = 10**9; N = int(input()); A = [*map(int, input().split())]; G = [[] for _ in range(N)]
for i in range(N):
    for j in map(int, input().split()[1:]): G[j-1].append(i)
for x in range(N):
    dp = [-10**9]*N
    for i in range(N-1, -1, -1):
        v = 0
        for j in G[i]:
            if v < dp[j]: v = dp[j]
        dp[i] = v+(i!=x)*A[i]
    V = min(V, dp[0])
print(V)