n = [*map(int, input())]; t = None
for i in range(len(n)-1, -1, -1):
    if t: continue
    if n[i]:
        for j in range(i-1, -1, -1):
            if n[j] < 9: t = (i, j); break
if t: n[t[0]] -= 1; n[t[1]] += 1; n[t[1]+1:] = sorted(n[t[1]+1:])
else:
    s = sum(n)-1; n = [1]+[0]*len(n); p = len(n)-1
    while s: u = min(9, s); s -= u; n[p] = u; p -= 1
print(''.join(map(str, n)))