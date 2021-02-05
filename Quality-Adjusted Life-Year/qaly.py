n = int(input())
result = 0
for _ in range(n):
    a,b = input().split(" ")
    result += float(a)*float(b)
print(result)