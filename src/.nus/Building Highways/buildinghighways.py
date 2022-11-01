n, arr = int(input()), list(map(int, input().split()))
print(min(arr)*(n-2) + sum(arr))