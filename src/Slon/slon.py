A=input();x=1;P,M=map(int,input().split());t=eval(A);x=0;b=eval(A)
while((t-b)*x+b)%M-P:x+=1
print(x)