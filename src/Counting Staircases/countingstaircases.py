n, m, *a = map(int, open(0).read().split()); print(1+(n-2*m+1)//(2*m-2)); a.sort(reverse=1); v = []; b = []
for _ in range(2*m-1): b.append(a.pop())
b.reverse(); v = b[m-1::-1]+b[m:]
while a:
    b = []
    for _ in range(min(2*m-2, len(a))): b.append(a.pop())
    b.reverse(); v.extend(b[m-2::-1]+b[m-1:])
print(*v)