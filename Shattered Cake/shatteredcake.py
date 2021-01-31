w = int(input())
n = int(input())
area = 0
for _ in range(n):
    a,b = input().split(" ")
    area += int(a)*int(b)
print(area//w)