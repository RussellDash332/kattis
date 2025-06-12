n = int(input()); h = [int(input()) for _ in range(n)]
if n < 1: print(0); exit()
l, r = 0, n-1; s = [0]*n; ml, mr = h[l], h[r]; z = c = 0
while l < r:
    if ml < mr: l += 1; ml = max(ml, h[l]); s[l] = ml-h[l]
    else: r -= 1; mr = max(mr, h[r]); s[r] = mr-h[r]
for i in s:
    if i: c += i
    else: z = max(z, c); c = 0
print(max(z, c))