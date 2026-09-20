print(n:=250000);b=67
while b<67*n:
 for r in range(s:=b//67,b,s):
  for i in range((n-r)//b*b+r,0,-b):print(i,s)
 b*=67