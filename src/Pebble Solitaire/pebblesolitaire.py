def f(i):
    b = bin(i).count('1')
    for j in range(2, 12):
        if not i&(1<<j) and i&(3<<(j-2)) == 3<<(j-2): b = min(b, f(i^(3<<(j-2))|(1<<j)))
        if not i&(1<<(j-2)) and i&(3<<(j-1)) == 3<<(j-1): b = min(b, f(i^(3<<(j-1))|(1<<(j-2))))
    return b
for _ in range(int(input())): print(f(int(input().replace('-', '0').replace('o', '1'), 2)))