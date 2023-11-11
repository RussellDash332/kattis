s = input().strip()[::-1]; v = []
if s[0] != 'O' or 'OO' in s or {*s} != {*'OE'}: print('INVALID'), exit(0)
for i in range(4, 100, 2):
    n = 1<<i; ok = 1
    for j in s:
        if j == 'O':
            if n%3 == 1: n //= 3
            else: ok = 0; break
        else: n *= 2
    if ok*n: v.append(n)
print(min(v, default='INVALID'))