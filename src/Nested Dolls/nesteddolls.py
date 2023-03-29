for _ in range(int(input())):
    d, arr, ans = int(input()), list(map(int, input().split())), 0
    dp = [0]*d # dp[i] = largest doll of LIS that starts at idx i
    for _, h in sorted((arr[i], -arr[i+1]) for i in range(0,2*d,2)): # increasing w, decreasing h
        lo, hi = 0, ans
        while hi > lo:
            m = (lo + hi)//2
            if dp[m] < -h: hi = m
            else: lo = m + 1
        dp[lo] = -h # note to self: first-point trick
        ans += lo == ans
    print(ans)