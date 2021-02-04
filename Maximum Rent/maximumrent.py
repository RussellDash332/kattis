def f(x,y,a,b):
    return a*x+b*y

a,b = list(map(int,input().split(" ")))
m,s = list(map(int,input().split(" ")))
x,y = s-m,2*m-s

if s <= m+1:
    print(max(f(m-1,1,a,b),f(1,m-1,a,b),f(1,max(s-2,1),a,b)))
elif s <= 2*m-1:
    print(max(f(x,y,a,b),f(m-1,1,a,b)))
else:
    print(0)