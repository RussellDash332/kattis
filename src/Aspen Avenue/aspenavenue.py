import sys

n = int(input())
ll, w = map(int, input().split())
arr = []
for line in sys.stdin:
    arr.append(int(line))
arr.sort()

dp = []
llp = ll / (n//2 - 1)
for i in range(n//2 + 1):
    dp.append([10**9] * (n//2 + 1))
dp[0][0] = 0
for i in range(1, n//2 + 1):
    dp[i][0] = dp[i - 1][0] + abs(arr[n - i] - llp * (n//2 - i))
    dp[0][i] = dp[0][i - 1] + ((arr[n - i] - llp * (n//2 - i))**2 + w**2)**0.5
for i in range(1, n//2 + 1):
    for j in range(1, n//2 + 1):
        dp[i][j] = min(
            dp[i - 1][j] + abs(arr[n - i - j] - llp * (n//2 - i)),
            dp[i][j - 1] + ((arr[n - i - j] - llp * (n//2 - j))**2 + w**2)**0.5
        )

print(dp[-1][-1])