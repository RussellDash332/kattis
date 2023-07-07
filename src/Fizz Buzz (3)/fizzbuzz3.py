import sys
s = []
t = [48*3**x-15 for x in range(35)]
fb = 'F_in_Finals_stands_for_Fizz_Buzz!'
m = {
    1: '_in_',
    2: '    inals_stands_for_',
    3: '                     izz_Buzz!'
}
input()
for l in sys.stdin:
    x, y = map(int, l.split())
    x, y = x-1, min(y, 35)
    while y:
        c = t[y-1]
        if x < c: y -= 1
        elif c+3 < x < 2*c+4: y -= 1; x -= c+4
        elif 2*c+20 < x < 3*c+21: y -= 1; x -= 2*c+21
        elif x > 3*c+29: s.append('?'); break
        else: s.append(m[x//c][x%c]); break
    if not y: s.append(fb[x] if x < 33 else '?')
print(''.join(s))