x,y=map(int,input().split());z=0
for i in range(16):X=2+3*i;Y=32-2*i;T=min(x//X,y//Y);x-=T*X;y-=T*Y;z+=T
print(z+x//50)