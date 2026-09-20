for _ in'.'*int(input()):
 n,x=map(int,input().split())
 for t in range(67):
  if x==1:print(t);break
  x=x*x%n
 else:print('impossible')