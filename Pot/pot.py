q = int(input())
res = 0
for _ in range(q):
    p = int(input())
    res += (p//10)**(p%10)
print(res)