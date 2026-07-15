I=lambda:map(int,input().split());x,*a=I();y,*b=I();z,*c=I();l,h=max(a+b+c)+1,2**61
def f(p):
 X=Y=Z=0
 for i in a:X=X*p+i
 for i in b:Y=Y*p+i
 for i in c:Z=Z*p+i
 return X*Y-Z
while l<h:
 if f(m:=(l+h)//2)>0:l=m+1
 else:h=m
print(['impossible',l][f(l)==0])