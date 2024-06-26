def dp(pos, tie):
    if pos == len(s): return 1
    ans = 0
    for i in '02':
        if tie: ans += 1<<(len(s)-pos-1)
        elif i == s[pos]: ans += dp(pos+1, 0)
        elif i < s[pos]: ans += dp(pos+1, 1)
    return ans
s = input(); print(dp(0, 0))