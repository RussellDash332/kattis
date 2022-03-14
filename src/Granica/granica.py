import sys
input()

nums = []
for line in sys.stdin:
    nums.append(int(line))
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

m = nums[0] - nums[1]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        m = gcd(m, abs(nums[i] - nums[j]))
        
def div(m):
    res = []
    d = 1
    while d**2 <= m:
        if m % d == 0:
            if d != 1:
                res.append(d)
            if d**2 != m:
                res.append(m // d)
        d += 1
    return res
    
print(*div(m))