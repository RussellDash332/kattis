from array import*;import sys;from collections import*;C,R,c,r,*M=map(int,sys.stdin.read().split());Z={r*C+c};Q=deque([r*C+c]);M=array('b',M)
while Q:
 r,c=divmod(Q.popleft(),C)
 for i,j in((0,-1),(0,1),(1,0),(-1,0)):
  if R>r+i>-1<c+j<C and M[r*C+c]==M[(r+i)*C+c+j]and(r+i)*C+c+j not in Z:Q.append((r+i)*C+c+j);Z.add(Q[-1])
for x in sorted(Z):sys.stdout.write(f'{x%C} {x//C}\n')