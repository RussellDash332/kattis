import sys
for s in sys.stdin:
    s = s.strip(); r = set(); n = len(s)
    dp = [[0]*(n+1) for _ in range(n)]
    for i in range(n): dp[i][i] = dp[i][i+1] = 1
    for i in range(n-1, -1, -1):
        for j in range(i+2, n+1):
            dp[i][j] = (s[i]==s[j-1])*dp[i+1][j-1]
            if dp[i][j]: r.add(s[i:j])
    for i in sorted(r): sys.stdout.write(i+'\n')
    print()