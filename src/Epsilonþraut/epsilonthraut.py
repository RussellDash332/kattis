a,b=map(float,input().split())
if a+1>b:print('Engin lausn!');exit()
if a+1==b:print(1,a);exit()
for n in range(2,10**6+1):
 if(c:=b**(1/n))*n<=a+n:S=a+n-(n-2)*c;P=c*c;d=S*S-4*P;print(n,*[c-1]*(n-2),(S+d**.5-2)/2,(S-d**.5-2)/2);break
else:print('Engin lausn!')