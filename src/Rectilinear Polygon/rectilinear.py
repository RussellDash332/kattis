import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input()); ans = 0
    p = [[*map(int, input().split())] for _ in range(n)]
    if n % 2: print(-1); continue
    px = sorted(p); py = sorted(p, key=lambda x: (x[1], x[0])); ok = 1
    for i in range(0, n, 2):
        if px[i][0] != px[i+1][0] or py[i][1] != py[i+1][1]: ok = 0; break
        ans += abs(px[i][0]-px[i+1][0]) + abs(px[i][1]-px[i+1][1]) + abs(py[i][0]-py[i+1][0]) + abs(py[i][1]-py[i+1][1])
    if min(len({*(i[0] for i in px)}), len({*(i[1] for i in px)})) < 3: ok = 0
    print(ans if ok else -1)