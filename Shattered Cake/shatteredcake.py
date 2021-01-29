w = int(input())
n = int(input())
area = 0
for _ in range(n):
    a,b = map(int,input().split(" "))
    area += a*b
print(area//w)