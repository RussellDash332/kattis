m, b, s = map(int, input().split())
B = [int(input(), 2) for _ in range(b)]
S = 0
for k in B:
    if k>>(s-m)&1: S |= k
print((S.bit_count() or 1)-1)