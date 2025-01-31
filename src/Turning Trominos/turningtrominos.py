for _ in'.'*int(input()):
 x,y=map(int,input().split());m=1<<61;o=0
 while m:
  if x//m<4>y//m:
   b=1<<(x//m*4+y//m);x%=4*m;y%=4*m
   if b&140:o+=1;x,y=4*m-1-y,x
   if b&12544:o-=1;x,y=y,4*m-1-x
   if b&608:x,y=x-m,y-m
  m>>=1
 print(o%4)