import sys; input = sys.stdin.readline
N = int(input()); R = []
for i in map(int, input().split()):
    lo, hi = 0, len(R)
    while lo<hi:
        if R[-1-(mi:=(lo+hi)//2)][-1] < i: lo = mi+1
        else: hi = mi
    if lo == 0: R.append([i])
    else: R[-lo].append(i)
print(len(R))
for i in R: print(*i)