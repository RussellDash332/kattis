import sys; input = sys.stdin.readline
while True:
    S, x, y, dx, dy = map(int, input().split()); t = 0
    if S < 1: break
    while True:
        m = x%(2*S); n = y%(2*S)
        if (S<m<2*S and 0<n<S) or (S<n<2*S and 0<m<S): break
        t += 1; x += dx; y += dy
        if t == 10000: break
    if t < 10000: print(f'After {t} jumps the flea lands at ({x}, {y}).')
    else: print('The flea cannot escape from black squares.')