t,n,*a=map(int,open(l:=0));h=10**18
while l<h:
 m=(l+h)//2
 if sum(m//i for i in a)<t:l=m+1
 else:h=m
print(l)