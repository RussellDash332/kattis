import sys

def prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

nums = []
for line in sys.stdin:
    line = line.strip().split()
    for i in line:
        try:
            nums.append(int(i))
            if str(int(i)) != i:
                raise Exception
        except:
            print(0)
            sys.exit(0)
print(int(
    len(nums) == 3 and
    nums[0] == nums[1] + nums[2] and
    nums[0] % 2 == 0 and
    3 < nums[0] <= 10**9 and
    prime(nums[1]) and prime(nums[2])
))