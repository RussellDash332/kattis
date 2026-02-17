n, m = map(int, input().split())
P = [[*map(eval, input().split())] for _ in range(n)]
R = [[*map(eval, input().split())] for _ in range(m)]
print(max(abs(w*h-sum(x<=w and y<=h for x, y in P)/n) for w, h in R))