def q(a,b,c,d):print('?',a,b,c,d);return int(input())
def f(l,r):
 if l>=r-1:return q(0,0,l,r)
 x=l;y=r-1
 while x<y:
  k=q(l,m:=(x+y+1)//2,m,r)
  if k==0:return 2*f(l,m)
  if k>0:x=m
  else:y=m-1
 return 2*(f(l,x)if l+r>x*2else f(x+1,r))+1
print('!',f(0,int(input())))