n = int(input())
arr = list(map(int, input().split()))

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

res = {arr[0]}
temp = {arr[0]}
for i in range(1, n):
    temp2 = {arr[i]}
    for v in temp:
        temp2.add(gcd(v, arr[i]))
    res |= temp2
    temp = temp2

print(len(res))