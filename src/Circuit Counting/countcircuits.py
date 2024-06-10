N = int(input()); P = []; K = {}
for _ in range(N): x, y = map(int, input().split()); P.append((x, y))
def dp(i, cx, cy):
    if i == N: return cx == cy == 0
    if (t:=(i, cx, cy)) in K: return K[t]
    x, y = P[i]; K[t] = dp(i+1, cx, cy)+dp(i+1, cx+x, cy+y); return K[t]
print(dp(0, 0, 0)-1)