import sys; input = sys.stdin.readline
n = int(input()); h = [*map(int, input().split())]
m = int(input()); b = [*map(int, input().split())]
c = max(b); dp = [0]*(c+1); dp[0] = 1
for i in range(1,n+1):
    for j in range(1,c+1):
        if j >= h[i-1]: dp[j] += dp[j-h[i-1]]
for c in b:
    if dp[c] == 0: print('Impossible')
    elif dp[c] > 1: print('Ambiguous')
    else:
        menu = []; s = c; t = n
        while s:
            if h[t-1] <= s and dp[s-h[t-1]] == 1: menu.append(t); s -= h[t-1]
            else: t -= 1
        print(*menu[::-1])