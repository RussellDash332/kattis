import sys;G=sys.stdin.readline
R,C=map(int,G().split());M=[G()for _ in'.'*R];D=[];I=Z=10**9;K=range
if R>C:M=[*map(list,zip(*M))];R,C=C,R
for i in K(R):
 for c in'WALDO':
  N=[I]*-~C
  for j in K(C)[::-1]:N[j]=[N[j+1],j][M[i][j]==c]
  N.pop();D+=N
for i in K(R):
 P=[I]*5*C
 for h in K(1,R-i+1):
  for c in K(C):
   for w in K(5):P[5*c+w]=min(P[5*c+w],D[(i+h-1)*5*C+C*w+c])
   Z=min(Z,h*(max(P[5*c:5*c+5])-c+1))
print(['impossible',Z][Z<10**6])