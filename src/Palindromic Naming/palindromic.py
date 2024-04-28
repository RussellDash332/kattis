import sys; input = sys.stdin.readline
M = 10**9+7

def cnt(s):
    dp = [[0]*len(s) for _ in range(len(s))]
    for i in range(len(s)): dp[i][i] = 1
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            dp[i][j] = dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
            if s[i] == s[j]: dp[i][j] += dp[i+1][j-1]+1
            dp[i][j] %= M
    return dp[0][-1]

for _ in range(int(input())): print(cnt(input().strip()))