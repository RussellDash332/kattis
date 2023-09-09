s1 = input(); s2 = input()
dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
for i in range(len(s1)+1):
    for j in range(len(s2)+1):
        if i == 0: dp[i][j] = j
        elif j == 0: dp[i][j] = i
        elif s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]+1
        else: dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
i = len(s1); j = len(s2); a = []
while i and j:
    if s1[i-1] == s2[j-1]: a.append(s1[i-1]); i -=1 ; j -= 1
    elif dp[i-1][j] > dp[i][j-1]: a.append(s2[j-1]); j -= 1
    else: a.append(s1[i-1]); i -= 1
while i: a.append(s1[i-1]); i -= 1
while j: a.append(s2[j-1]); j -= 1
print(''.join(a[::-1]))