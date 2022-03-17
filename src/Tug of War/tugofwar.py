import sys

n = int(input())
p = []
for line in sys.stdin:
    p.append(int(line))
s = sum(p)

# dp[i][j] = True if I can assign i people with total sum j on a team, then check for i = n // 2 only
dp = []
for _ in range(n // 2 + 1):
    dp2 = []
    for _ in range(s + 1):
        dp2.append(False)
    dp.append(dp2)

dp[0][0] = True
# Check for every person given an initial configuration
for w in p:
    for i in range(n // 2 - 1, -1, -1):
        for j in range(s - w, -1, -1):
            if dp[i][j]:
                dp[i + 1][j + w] = True

left, diff = 0, s
for tw in range(s + 1):
    if dp[n // 2][tw] and abs(s - 2 * tw) < diff:
        left, diff = tw, abs(s - 2 * tw)
if left > s - left:
    left = s - left
print(left, s - left)