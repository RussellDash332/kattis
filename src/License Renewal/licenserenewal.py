n, s1, s2, *a = map(int, open(s:=0).read().split())
if s1 > s2: s1, s2 = s2, s1
d = [1]+[0]*s1; z = 0
for i, e in enumerate(a):
    s += e
    for j in range(s1-e, -1, -1): d[j+e] |= d[j]
    k = s1
    while d[k]<1: k -= 1
    if s-k <= s2: z = i+1
print(z)