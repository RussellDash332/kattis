import sys; input = sys.stdin.readline
P = [[], [], []]
for _ in range(int(input())): x, y, c = input().split(); x = int(x); y = int(y); P[ord(c)%3].append((x, y, (x*x+y*y)**.5))
print(min(sum(min(r+((x2-x)**2+(y2-y)**2)**.5 for x2, y2, r in P[(i+j+1)%3]) for j in range(2)) for i in range(3) for x, y, _ in P[i]))