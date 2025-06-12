m={0:0,1:1,6:9,8:8,9:6};s=[]
for _ in range(int(input())):
 v=input()
 if all(int(i)in m for i in v):v=min(v,''.join(str(m[int(i)])for i in v[::-1]))
 s.append(v)
from functools import*;print(''.join(sorted(s,key=cmp_to_key(lambda x,y:1-2*(x+y<y+x)))))