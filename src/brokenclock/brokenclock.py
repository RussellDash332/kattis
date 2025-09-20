from itertools import*;b=[119,18,93,91,58,107,111,82,127,122];z=[]
for _ in'.'*6:
 s=input()[::2];f=s.replace
 try:z+=[[b.index(int(s,2))]]
 except:z+=[[i for i in range(10)if(b[i]^int(f('-','0'),2))&int(f('0','1').replace('-','0'),2)<1]]
for a,b,c,d,e,f in product(*z):10*a+b<24>6>c<6>e!=print(f'{a}{b}:{c}{d}:{e}{f}')