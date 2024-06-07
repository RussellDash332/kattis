import sys; input = sys.stdin.readline
W, L, N = map(int, input().split()); U = set(); z = 0
for _ in range(N):
    K = []; S = []; t = [*map(int, input().split())]; b = [*map(int, input().split())]; o = min(b); p = min(t)
    for i in range(L): K.append((b[i]-o, W-b[i]-t[i])); S.append((t[i]-p, W-b[i]-t[i]))
    R = tuple(K[::-1]); T = tuple(S[::-1]); K = tuple(K); S = tuple(S); z += R not in U and T not in U and K not in U and S not in U; U.add(R); U.add(T); U.add(K); U.add(S)
print(z)