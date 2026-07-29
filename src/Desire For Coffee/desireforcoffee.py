N = int(input()); T = []; D = [-10**9]*567
for _ in range(N): c, w, l = map(int, input().split()); T.append((-w-c, w, l))
for n, w, l in sorted(T):
    for i in range(w, 567): k = min(i, -n)-w; D[k] = max(D[k], D[i]+l)
    D[-n-w] = max(D[-n-w], l)
print(max(D))