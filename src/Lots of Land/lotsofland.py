h,w,n=map(int,input().split())
if h*w%n:print('impossible');exit()
for a in range(1,h+1):
 if h*w%(n*a)<1>h%a:
  b=h*w//n//a
  if w%b<1:print('\n'.join(''.join(chr(65+(i//a)*(w//b)+j//b)for j in range(w))for i in range(h)));break