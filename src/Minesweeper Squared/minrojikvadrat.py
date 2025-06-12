n=int(input())-2;d=[]
if n%3==0 or n<0:print(0);exit()
for _ in'.'*4:d.extend([v:=3-n%3]*2+(n//3+v%2)*[3])
print(len(d),s:=1)
for i in d[1:]:print(s:=s+i)