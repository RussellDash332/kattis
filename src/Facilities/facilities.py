N, T = map(int, input().split())
W = [0]*(T+2000)
for _ in range(N):
    b, d = map(int, input().split())
    l, r = b, b+d; z = s = 0
    while l < T:
        W[l] += 1; W[r] -= 1
        l += b+d; r += b+d
for i in W: z = max(z, s:=s+i)
print(z)