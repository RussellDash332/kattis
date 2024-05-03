n = int(input()); w = 'ETILLETA'; dp = [0]*9; v = [0]; dp[0] = 1; s = []
while v[-1] <= n:
    for i in range(8):
        for j in range(7, -1, -1): dp[j+1] += dp[j]*(w[i]==w[j])
    v.append(dp[8])
while v[-1]: x = v.pop(); s.append('S'*(n//x)); n %= x; s.append(w[::-1])
print(''.join(s))