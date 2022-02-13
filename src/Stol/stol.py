r, c = list(map(int, input().split()))
hists, hist = [], [0] * c

for _ in range(r):
    s = input()
    for i in range(c):
        if s[i] == '.':
            hist[i] += 1
        else:
            hist[i] = 0
    hists.append(hist.copy())

def max_perimeter(h):
    stack = []
    idx = 0
    result = 0
    while idx < len(h):
        if not stack or h[stack[-1]] <= h[idx]:
            stack.append(idx)
            idx += 1
        else:
            top = stack.pop()
            if stack and h[top] != 0:
                result = max(result, 2 * (h[top] + (idx - stack[-1] - 1)) * int(h[top] != 0))
            else:
                result = max(result, 2 * (h[top] + idx) * int(h[top] != 0))
    while stack:
        top = stack.pop()
        if stack:
            result = max(result, 2 * (h[top] + (idx - stack[-1] - 1)) * int(h[top] != 0))
        else:
            result = max(result, 2 * (h[top] + idx) * int(h[top] != 0))
    return result

ans = 0
for h in hists:
    ans = max(ans, max_perimeter(h))
print(ans - 1)