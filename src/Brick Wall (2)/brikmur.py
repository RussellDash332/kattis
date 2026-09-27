from functools import*;Z=0
@cache
def f(a,b,c,x,y):
 global Z
 if x>y:x,y=y,x
 for i in(0,1,2):
  if(a,b,c)[i]:
   if(z:=2<<i)+x-y:f(a-(i<1),b-i%2,c-i//2,x+z,y)
   else:Z=max(Z,y)
f(*map(int,input().split()),0,0);print(Z)