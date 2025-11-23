I=lambda:map(int,input().split());n,q=I();F=[0]*-~n;z=lambda i:F[i]+z(i&~-i)if i else 0
def p(i):
 while i<=n:F[i]+=a;i+=i&-i
for i,a in enumerate(A:=[*I()]):p(i+1)
for _ in'.'*q:
 t,x,y=I();l=x=x-1;h=n+1
 if t%2:a=y-A[x];p(x+1);A[x]=y;continue
 while l<h:
  if z(min(m:=(l+h)//2,n))-z(x)>y:h=m
  else:l=m+1
 print(~x+l)