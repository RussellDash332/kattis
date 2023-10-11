import sys
input()

c = 1
fl = True
for line in sys.stdin:
    if fl:
        fl = False
        print('Case', c)
        moolah = []
        n, m, l = map(int, line.split())
    else:
        an, ab = line.split(':')
        a, b = map(int, ab.split(','))
        temp = n - m
        x = float('inf')
        k = 0
        while temp >= 0:
            x = min(x, b*k + a*temp)
            temp = (temp + m) // 2 - m
            k += 1
        moolah.append((an, x))
        l -= 1
        if l == 0:
            moolah.sort(key=lambda x: (x[1], x[0]))
            for ag in moolah:
                print(*ag)
            fl = True
            c += 1