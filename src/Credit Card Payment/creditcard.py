import sys; input = sys.stdin.readline
for _ in range(int(input())):
    r, b, m = map(lambda x: round(float(x)*100), input().split()); r = 1+r/1e4
    for t in range(1, 1201):
        b = b*r-m; b = int(b)+(b-int(b)>=0.5-1e-8)
        if b <= 0: break
    if b > 0: print('impossible')
    else: print(t)