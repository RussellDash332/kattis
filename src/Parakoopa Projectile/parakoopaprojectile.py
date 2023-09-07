b = 1e19; p = sorted([*map(int, input().split())] for _ in range(int(input())))
for i in range(len(p)-1):
    x1, y1 = p[i]; x2, y2 = p[i+1]
    if x1 == x2 or (r:=y1*x2-y2*x1) == 0 or r/(x1-x2) > 0: continue
    b = min(b, (y1*x2*x2-y2*x1*x1)/r)
print(b)