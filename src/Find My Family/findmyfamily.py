t = int(input())
ok = []
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    stack = [arr[0]]
    record = float('inf')
    for j in range(1, n):
        if stack and arr[j] < stack[-1]:
            while stack and stack[-1] > arr[j]:
                record = min(record, stack.pop())
        elif arr[j] > record:
            ok.append(i + 1)
            break
        stack.append(arr[j])

print(len(ok))
for idx in ok:
    print(idx)