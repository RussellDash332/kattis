from random import*;w,H=map(int,input().split());c=(H,w)
for x in sample(range(1,w+1),w):
 if c[0]<1:break
 if input(f'? {x} {H-c[0]+1}\n')>'c':continue
 l,h=0,c[0]-1
 while l<h:
  m=(l+h)>>1
  if input(f'? {x} {H-m}\n')<'c':h=m
  else:l=m+1
 c=min(c,(l,x))
y,x=c;print('!',x,H-y)