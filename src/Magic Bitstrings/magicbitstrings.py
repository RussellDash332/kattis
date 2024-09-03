while(p:=int(input())):
 if p==2:print('Impossible');continue
 v=[1]*p
 for i in range(p):v[i*i%p]=0
 print(''.join(map(str,v[1:])))