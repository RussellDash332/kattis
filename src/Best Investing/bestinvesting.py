r,y,d,w=map(int,input().split());r=1+r/100;b=z=0
for x in range(y+1):
 b*=r;c=w*(1-r**(x-y))/(r-1)-b
 if c>0:u=min(d,c);b+=u;z-=u
 else:u=min(w,b,-c);b-=u;z+=u
print(z)