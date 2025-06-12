z, x, y = map(int, input().split())
m = [[' ']*(x+y-1) for _ in range(y+z-1)]
for i in range(1, x-1):
    for r, c in ((~0, i), (~(z-1), i), (0, ~i), (z-1, ~i)): m[r][c] = '-'
for i in range(1, z-1):
    for r, c in ((i, ~0), (i, ~(x-1)), (~i, 0), (~i, x-1)):
        if m[r][c] == '-': m[r][c] = 'x'
        else: m[r][c] = '|'
for i in range(1, y-1):
    for r, c in ((~0-i, i), (~(z-1)-i, i), (~0-i, (x-1)+i), (~(z-1)-i, (x-1)+i)):
        if m[r][c] in '|-x': m[r][c] = 'x'
        else: m[r][c] = '/'
for r in (~0, ~(z-1)):
    for c in (0, x-1): m[r][c] = m[r-y+1][c+y-1] = '+'
print(*map(lambda x: ''.join(x).rstrip(), m), sep='\n')