X=Y=0
for i in range(int(input())):
 x,y=map(int,input().split('-'))
 if(x+y)%4in(1,2):x,y=y,x
 (x<X)+(y<Y)+(11in(X,Y))*(x>X or y>Y)+(x==y==11)and print('error',i+1)<exit();X,Y=x,y
print('ok')