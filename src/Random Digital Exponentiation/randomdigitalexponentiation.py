def bt(a, b, e):
    if a == b == 0: print(*e[::-1]), exit(0)
    i, m = 0, 1
    while True:
        if m > b: break
        if m%10 == b%10: e.append(i), bt(a//10, (b-m)//10, e), e.pop()
        i += 1; m *= a%10
        if a%10 < 2: break
bt(*map(int, input().split()), [])