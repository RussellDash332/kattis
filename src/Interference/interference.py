import sys; input = sys.stdin.readline
n, w = map(int, input().split()); A = []
for _ in range(n):
    c, *r = input().split()
    if c == '!': p, l, a = map(int, r); A.append((p, l, a))
    else:
        x = int(r[0]); z = 0
        for p, l, a in A:
            if p <= x < p+l: z += (a, 0, -a, 0)[(p-x)%4]
        print(z)