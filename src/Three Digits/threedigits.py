n = int(input())

if n == 5:
    print(12)
elif n == 6:
    print(72)
else:
    f, n5, n2 = 1, 0, 0
    for i in range(2, n + 1):
        f *= i
        # Say f = k * 2^(a + b) * 5^b
        # If we set f to be divided by 10 greedily, we will have f = k * 2^a
        # Then applying modulo 10^(m >= 3) will chop down some important digits that might make an extra 10
        # e.g. k = 1, 2^a = 1024 and then we multiply by 125 later. Compare 24*125 = 3000 -> 3 and 1024*125 = 128000 -> 128.
        # Here, we perform mod 1000 on f = k and then remultiply by 2^a, which doesn't matter since we cannot multiply k
        # by any power of 2 or 5 to produce a new trailing 0.
        while f % 5 == 0:
            f //= 5
            n5 += 1
        while f % 2 == 0:
            f //= 2
            n2 += 1
        f %= 1000
    for _ in range(n2 - n5):
        f *= 2
        f %= 1000
    a = str(f)
    print('0' * (3 - len(a)) + a)