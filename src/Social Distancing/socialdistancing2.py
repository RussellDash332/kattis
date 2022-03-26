s, _ = map(int, input().split())
arr = list(map(int, input().split()))
ans = (arr[0] + s - arr[-1] - 2) // 2
for i in range(1, len(arr)):
    ans += (arr[i] - arr[i - 1] - 2) // 2
print(ans)