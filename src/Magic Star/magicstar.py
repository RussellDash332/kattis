from math import*;s=[i for i in open(0).read() if i.isalpha()];z=[0]*12;T=1<<26
for i in range(12):z[i]=s[i].isupper()<<(ord(s[i])-64)
def f(b,i):
 if i>11<prod(z[j]for j in(1,5,8,11))==T==prod(z[j]for j in(4,6,9,11)):Z=[*map(lambda x:chr(x.bit_length()+63),z)];print(f'....{Z[0]}....\n.{Z[1]}.{Z[2]}.{Z[3]}.{Z[4]}.\n..{Z[5]}...{Z[6]}..\n.{Z[7]}.{Z[8]}.{Z[9]}.{Z[10]}.\n....{Z[11]}....');exit()
 if i>4<T!=prod(z[j]for j in(1,2,3,4))or i>7<T!=prod(z[j]for j in(0,2,5,7))or i>10<T!=prod(z[j]for j in(7,8,9,10))or i>10<T!=prod(z[j]for j in(0,3,6,10))or i>11:return
 if z[i]:return f(b,i+1)
 b2=b
 while b:u=b&-b;z[i]=u;f(b2^u,i+1);z[i]=0;b^=u
f(8190-sum(z),0)