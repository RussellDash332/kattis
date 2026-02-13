N,P,*C=map(int,open(p:=0).read().split());O=[Z:=0]*6
for c in C:p+=c;Z|=p>P;O[0]+=c//5;O[5-c%5]+=1;d=sum(i*O[i]for i in range(5));s=sum(O[:5]);O=[0]*6;i=5;exec("u=min(d//i,s);d-=i*u;s-=u;O[i]=u;i-=1;"*5);u=min(p//5,s);O[0]=s-u;p-=5*u
print(['No o','O'][Z]+'verflow')