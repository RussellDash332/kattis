for _ in'.'*int(input()):
 n,d=map(int,input().split());k=0;m=1
 while m<n:k+=1;m*=d+1
 print(k)