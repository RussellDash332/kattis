n,p,r,B=map(int,input().split());a,b=1,n+1
def f(x):l=n%x;m=~-n//x+1;t=n//x;return p*~-x+r*n+((x-l)*t*~-t+l*m*~-m)*B//2
while b-a>2:
 if f(m:=b-(b-a)//3)>f(l:=a+(b-a)//3):b=m
 else:a=l
print(min(map(f,range(max(a-2,1),b+3))))