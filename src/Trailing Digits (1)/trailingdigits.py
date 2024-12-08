b, d, a = input().strip().split()
m = 0; n = 1; p = 1; b = int(b); d = int(d); best = 0

def gcd(a, b):
    while b: a, b = b, a % b
    return a

for l in range(len(a)): # O(log10 a)
    # 10**l * x + d * (10**l-1)//9 = 0 (mod k) for all k that divides b
    # p*x + d*m = 0 (mod b) -> need to find this in O(log2 b)
    # p*x = -d*m (mod b) but gcd(p, b) might not be 1
    g = gcd(p, b) # O(log b)
    if -d*m%b%g == 0:
        x = -d*m//g*pow(p//g, -1, b//g)%(b//g)
        if x == 0: x += b//g # edge case: b//g is optimal rather than b
        t = 10**len(str(x))
        while x < t:
            r = f'{x}{str(d)*l}'; l2 = l; x2 = x
            while x2 % 10 == d: x2 //= 10; l2 += 1 # edge case if x also ends with some d's
            if len(r) < len(a) or (len(r) == len(a) and r <= a): best = max(best, l2)
            x += b//g
    m += p; p *= 10; p %= b; m %= b
print(best)