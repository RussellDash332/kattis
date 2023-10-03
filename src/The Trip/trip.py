import sys; input = sys.stdin.readline
while (n:=int(input())):
    p = [round(100*float(input())) for _ in range(n)]
    s = sum(p)//n; ov = v = 0
    for i in p:
        if i > s: ov += i-s; v += 1
    # There will be sum(p)%n people who has one extra cents
    # We took the excess money from v people
    # So we don't need to exchange the extra min(v, sum(p)%n) cents
    print('$'+'%.2f'%((ov-min(v, sum(p)%n))/100))