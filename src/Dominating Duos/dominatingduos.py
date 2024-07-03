s=[];a=0
for _ in'.'*int(input()):
 p=len(s);i=int(input())
 while s and s[-1]<i:s.pop()
 a+=p+min(0,1-len(s));s+=[i]
print(a)