# leetcode lmao
n, *height = map(int, open(0).read().split())
lo, hi = 0, len(height) - 1
best = 0
while lo < hi:
    l, r = height[lo], height[hi]
    best = max(best, min(l, r)*(hi - lo))
    if l < r:   lo += 1
    else:       hi -= 1
print(best)