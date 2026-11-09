R = [[*map(int, input().split())] for _ in '..']
def out(): print(*[f'({r[0]} {r[1]} {r[2]})' for r in R])
j = next(i for i in (0, 1, 2) if R[0][i+3] != R[1][i+3])
out()
for i in {0, 1, 2}-{j}:
    if R[0][i] == R[1][i]: R[0][i] += 1; out()
for i in (j, -~j%3, ~-j%3):
    z = 1
    while z:
        z = 0
        for r in R:
            d = (-1, 1)[r[i]<r[i+3]]
            if r[i] != r[i+3]: r[i] += d; z = 1
        out()