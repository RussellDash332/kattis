input();m=10**9+7;a=1;b=c=0;s=[*map(int,input())]
for i in s:t=[a,b,c];a,b,c=(a+t[-i%3])%m,(b+t[(1-i)%3])%m,(c+t[(2-i)%3])%m
print((a-pow(2,s.count(0),m))%m)