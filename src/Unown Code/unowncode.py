import sys; input = sys.stdin.readline
n = int(input()); arr = [*map(int, input().split())]
# the answer is guaranteed to be in a form of 2^a 5^b or 2^a 5^b + 1
MAX = 10**8
s = set(); a = 1
while a <= MAX:
    b = 1
    while a*b <= MAX: s.add(a*b), s.add(a*b+1); b *= 5
    a *= 2
s = sorted(s)[1:] # exclude 1
p = [[arr[i]] for i in range(n)]
for i in range(n):
    a = 1; d = 10**len(str(arr[i]))
    while a <= MAX: p[i].append(p[i][-1]**2%d); a *= 2
for ans in s:
    ok = 1
    for i in range(n):
        check = 1; d = 10**len(str(arr[i]))
        for j in range(len(p[i])):
            if ans&(1<<j): check = check*p[i][j]%d
        if check != arr[i]: ok = 0; break
    if ok: print(ans), exit(0)
print(-1)