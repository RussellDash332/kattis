z=m=0
for i,j in zip(*input().split()):z+=max(0,abs(d:=ord(j)-ord(i))-abs(m)*(m*d>0));m=d
print(z)