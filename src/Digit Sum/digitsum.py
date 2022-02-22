import sys
skip = input()

def d(n):
    res = 0
    num = list(map(int, str(n)))
    pos, mult = len(num) - 1, 1
    while pos >= 0:
        res += sum(num[:pos]) * num[pos] * mult
        res += num[pos] * (num[pos] - 1) // 2 * mult
        res += 45 * (mult // 10) * (len(num) - pos - 1) * num[pos]
        pos -= 1
        mult *= 10
    return res

for line in sys.stdin:
    a, b = list(map(int, line.split()))
    print(d(b + 1) - d(a))