import sys; input = sys.stdin.readline
n1, c1, s1, f1 = map(int, input().split())
S1 = input().strip()
F1 = [*map(lambda x: int(x)-1, input().split())]
T1 = [[*map(lambda x: int(x)-1, input().split())] for _ in range(n1)]

n2, c2, s2, f2 = map(int, input().split())
S2 = input().strip()
F2 = [*map(lambda x: int(x)-1, input().split())]
T2 = [[*map(lambda x: int(x)-1, input().split())] for _ in range(n2)]

# c1 == c2, S1 == S2
print(n1*n2, c1, (s1-1)*n2+s2, f1*f2)
print(S1)
print(*sorted(x1*n2+x2+1 for x1 in F1 for x2 in F2))
for i in range(n1*n2): print(*(T1[i//n2][j]*n2+T2[i%n2][j]+1 for j in range(c1)))