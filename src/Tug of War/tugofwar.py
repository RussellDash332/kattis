import sys

n = int(input())
p = []
for line in sys.stdin:
    p.append(int(line))
s = sum(p)

# j in dp[i] if I can assign i people with total sum j on a team, then check for i = n // 2 only
dp = []
for _ in range(n // 2 + 1):
    dp.append(set())

dp[0].add(0)
# Check for every person given an initial configuration
for w in p:
    for i in range(n // 2 - 1, -1, -1):
        for j in dp[i]:
            if j <= s - w:
                dp[i + 1].add(j + w)

left, diff = 0, s
for tw in dp[n // 2]:
    if abs(s - 2 * tw) < diff:
        left, diff = tw, abs(s - 2 * tw)
if left > s - left:
    left = s - left
print(left, s - left)