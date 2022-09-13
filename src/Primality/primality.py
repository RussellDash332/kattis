import random

def powmod(a, b, m):
    if b == 0:
        return 1
    elif b == 1:
        return a % m
    elif b % 2:
        return a * powmod(a * a % m, b // 2, m) % m
    return powmod(a * a % m, b // 2, m)
    
def is_prime(n, k):
    if n == 4: return "NO"
    if n in [2, 3]: return "YES"
    for i in range(k):
        if powmod(random.randint(2, n - 2), n - 1, n) != 1:
            return "NO"
    return "YES"
    
n = int(input())
k = 10**4
print(is_prime(n, k))