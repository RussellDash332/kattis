C,R=map(int,input().split());M=[input()for _ in'.'*(2*R+1)];Q=[2*(2*R*C-C+1)+(M[-2][1]=='L')];V={*Q}
for x in Q:
 u=x>>1;b=x&1;r=u//C;c=u%C
 if c>1and(t:=M[r][c-1])in'L.'and(z:=2*u-2+(b|(t=='L')))not in V:V.add(z);Q+=[z]
 if c<C-1and(t:=M[r][c+1])in'L.'and(z:=2*u+2+(b|(t=='L')))not in V:V.add(z);Q+=[z]
 if b and'.'==M[r-1][c]!=M[r+1][c]:
  if r<2:print('possible');exit()
  if(z:=2*u-4*C)not in V:V.add(z);Q+=[z]
 if'.'==M[r+1][c]and(z:=2*u+4*C)not in V:V.add(z);Q+=[z]
print('impossible')