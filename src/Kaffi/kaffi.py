n,w,*e=map(int,open(0).read().split());s=sum(e);l,h=1,max(e)
while l<h:
 m=(l+h)//2
 if sum(~-i//m+1for i in e)<=w:h=m
 else:l=m+1
print(w*l-s)