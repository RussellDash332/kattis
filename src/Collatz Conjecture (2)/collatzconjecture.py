def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
arr = list(map(int, input().split()))
D, d = {arr[0]}, {arr[0]}
for i in range(1, n):
    d = {gcd(v, arr[i]) for v in d} | {arr[i]}
    D |= d
print(len(D))