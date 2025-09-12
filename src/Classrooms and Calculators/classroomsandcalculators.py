from math import*;a,b,c,n=map(int,open(l:=0).read().split());h=10**10
while l<h:
 m=(l+h)//2
 if n>m-m//a-m//b-m//c+m//lcm(a,b)+m//lcm(b,c)+m//lcm(a,c)-m//lcm(a,b,c):l=m+1
 else:h=m
print(l)