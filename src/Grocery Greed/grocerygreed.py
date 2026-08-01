p=[T:=0]*5;input()
for i in input().split():k=round(float(i)*100);p[k%5]+=1;T+=k-k%5
a,b,c,d,e=p;u=min(d,e);d-=u;e-=u;print('%.2f'%((T+5*u+3*e+e//3+e%3+2*d+d//2+d%2)/100))