import sys
rev = [-1]*10000
for l in sys.stdin:
    nums = list(map(int, l.replace(':', '').split()))
    if nums[0] == 0: break
    n = int(nums[0])
    have = 0
    for i in range(1, n+1): rev[nums[i]] = i-1
    for i in range(1, n):
        for j in range(n-2*i):
            have = (rev[j] < rev[j+i]) ^ (rev[j+i] > rev[j+2*i])
            if have: break
        if have: break
    print(['yes', 'no'][have])