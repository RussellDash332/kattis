import sys; input = sys.stdin.readline; from bisect import *; from array import *
def gety(i):
    x1, y1, x2, y2 = S[i]; return y1+(y2-y1)*(cx-x1)/(x2-x1)
N = int(input()); E = []; L = 10**6+67; S = []; P = array('i', [-1]*-~N); T = array('I')
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    y1 += L; y2 += L
    if x1 > x2: x1, y1, x2, y2 = x2, y2, x1, y1
    E += [(x1, y1, i)]; E += [(x2, -y2, i)]; S += [(x1, y1, x2, y2)]
E += [(x0:=int(input()), 10**7+L, N)]; E += [(x0+1, ~L-10**7, N)]; S += [(x0, 10**7+L, x1, 10**7+L+1)]
for cx, y, i in sorted(E, key=lambda x: (x[0], x[1]<0, x[1])):
    if (y>0)==(S[i][3]>S[i][1]) and (p:=bisect_left(T, gety(i), key=gety)): P[i] = T[p-1]
    if y>0: insort(T, i, key=gety)
    else: T.remove(i)
c = N; x = S[N][0]
while ~P[c]: c = P[c]; x = S[c][2*(S[c][1]>S[c][3])]
print(x)