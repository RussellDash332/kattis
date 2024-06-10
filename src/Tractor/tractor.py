for _ in'.'*int(input()):
 A,B=map(int,input().split());s=p=0
 while p<=A+B:s+=min(A,p)+min(B,p)-p+1;p=2*p+1
 print(s)