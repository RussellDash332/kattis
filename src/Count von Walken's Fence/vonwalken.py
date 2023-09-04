d, n = map(float, input().split()); n = round(n); c = [*map(int, input().split())]; s = 0; mi, ma = 1, 0
for i in range(n): s += c[i]; mi = min(mi, d*(i+1)-s+1); ma = max(ma, d*(i+1)-s)
print('im'*(ma>mi)+'possible')