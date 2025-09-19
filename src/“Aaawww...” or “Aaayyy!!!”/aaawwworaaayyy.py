n, m, r = map(int, input().split())
v = [input() for _ in range(n)]
s = [(v[i].count('A'), v[i].count('P'), i) for i in range(n)]
c = [input().count('y')-3 for i in range(sum(p[1] for p in s))][::-1]
x = n-1
while c:
    while ~x and s[x][1]<1: x -= 1
    a, p, i = s[x]; z = c.pop()
    if z < 0: s[x] = (a, p-1, i)
    else: s.pop(x); s.insert(x-z, (a+1, p-1, i))
for i in range(n):
    if s[i][2] == r-1: print(i+1)