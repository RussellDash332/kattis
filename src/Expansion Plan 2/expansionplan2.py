I=input;n,q=map(int,I().split());a=[0];b=[0]
for e in I():a+=[a[-1]+(e<'5')];b+=[b[-1]+(e>'7')]
for _ in'.'*q:l,r,x,y=map(int,I().split());s=a[r]-a[l-1];t=b[r]-b[l-1];print('YNEOS'[2*t+s<abs(x)+abs(y)or t+s<max(abs(x),abs(y))::2])