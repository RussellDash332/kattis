z = []; m = 0
for _ in '.'*int(input()):
    s = input(); c = 1; p = q = 0
    for i in s:
        if i == s[0] and c: p += 2*(i<'R')-1
        else: c = 0; p = 2*p+2*(i<'R')-1; q += 1
    z.append((p, q)); m = max(m, q)
n = sum(p*2**(m-q) for p, q in z)
while n%2<1 and m: n //= 2; m -= 1
print(f'{n}/2^{m}' if m else n)