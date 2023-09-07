n, k = map(int, input().split())
s = sorted(map(int, input().split()), reverse=True)
sk = s[:k]; sr = s[k:]
best = (0, 0)
for d in range(1, s[0]+1):
    m = sum(i//d for i in sk)
    if m >= k: best = max(best, (d*k//2, -d*k//2))
    else:
        ss = sorted(sr + [i%d for i in sk if i%d], reverse=True)
        tt = ss[:k-m]+[d]*m
        while len(tt) < k: tt.append(0)
        tt.sort(reverse=True); best = max(best, (sum(tt[k//2:k]), -sum(tt[:k//2])))
print(best[0], -best[1])