C={};I=input
for _ in'.'*int(I()):k,v=I().split();C[k]=int(v)
for _ in'.'*int(I()):k,_,*r=I().split();C[k]=[r[::2],r[1::2]]
for _ in C:
 for k in C:
  if type(C[k])!=int and all(int==type(C[x])for x in C[k][0]):C[k]=sum(C[x]*int(y)for x,y in zip(*C[k]))
print(C['Capstone'])