n=int(input());L=[1,2,5,10,20,50,100,200,500];Z=[]
if n%2000in[0,4,40,44,404,400,440,444]:print('splittable')<exit()
while n:
 if(l:=L[-1])in[5,50,500]and(n//(u:=2*l//5))%2:Z+=[u]*(n//u);n%=u
 Z+=[l]*(n//l);n%=L.pop()
print(len(Z),*Z)