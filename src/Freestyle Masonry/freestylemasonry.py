n,k,*a=map(int,open(0).read().split());h=k
for i in a:
 e=h-i
 if e<0:h=0;break
 h=min(k,h-e%2*2+1)
print((e%2 or h<k)*'im'+'possible')