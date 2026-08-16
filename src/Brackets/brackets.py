from array import*;n=len(s:=input());D=array('B',[0]*3*(K:=n//2+2)*-~n);S=array('B',(x<')'for x in s))
if n%2:print('impossible');exit()
for t in(1,2,0):D[3*K*n+3*(n//2)+t]=1
for i in range(n-1,-1,-1):
 for l in range(n//2,-~i//2-1,-1):
  for t in(1,2,0):x=3*K*i+3*l+t;D[x]=(t<1==D[x-x%3+2])or(t>1==D[x-x%3+1])or D[x+3*K+3*((S[i]and t<2)or(1-S[i]and t>1))]
print('im'*(1-D[0])+'possible')