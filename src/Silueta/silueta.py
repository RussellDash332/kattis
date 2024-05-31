import sys; input = sys.stdin.readline
a = [0]*1001
for _ in range(int(input())):
    l, r, h = map(int, input().split())
    for i in range(l, r): a[i] = max(a[i], h)
while a and not a[-1]: a.pop()
for i in range(len(a)):
    if a[i]: a = a[i:]; break
a = [0]+a+[0]; P = 0
p = [['.']*len(a) for i in range(max(a)+1)]
for i in range(len(a)):
    p[a[i]][i] = '#'; P += bool(a[i])
    if i:
        P += abs(a[i-1]-a[i])
        if a[i-1] < a[i]:
            for j in range(a[i-1], a[i]): p[j][i] = '#'
        else:
            for j in range(a[i], a[i-1]): p[j][i-1] = '#'
print(P)
for x in p[:0:-1]: print(''.join(x[1:-1]))
print('*'*(len(a)-2))