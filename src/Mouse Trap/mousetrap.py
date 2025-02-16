import sys; input = sys.stdin.readline
N = int(input()); P = [[*map(int, input().split())] for _ in range(N)]
def cross(a, b): return a[0]*b[1]-a[1]*b[0]
A = Z = 0; S = [(0, 0)]
for i in range(N): S.append((S[-1][0]+P[i][0], S[-1][1]+P[i][1])); A += P[i][0]*P[(i+1)%N][1]-P[i][1]*P[(i+1)%N][0]
for i in range(N): Z += cross(((i-1)*P[i][0]-S[i][0], (i-1)*P[i][1]-S[i][1]), (S[-1][0]-S[i+1][0]-(N-i)*P[i][0], S[-1][1]-S[i+1][1]-(N-i)*P[i][1]))
print(abs(Z/A))