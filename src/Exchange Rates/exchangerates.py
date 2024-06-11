while(n:=int(input())):
 c=1e5;d=0
 for _ in'.'*n:r=float(input());c,d=max(c,int(d*r*0.97)),max(d,int(c/r*0.97))
 print('%.2f'%(c/100))