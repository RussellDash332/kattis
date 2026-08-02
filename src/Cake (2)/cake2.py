from math import*;R,a,b,c,d,e,f,g,h=map(int,open(0).read().split());t=atan2;A=sorted((t(b,a),t(d,c),t(f,e),t(h,g)));H=pi/2
for i in(0,1,2,3):s=A[i];r=A[i-1];q=A[i-2];p=A[i-3];max(z:=[p,q-H,r-2*H,s-3*H])-H<min(z)!=print('YES')<exit()
print('NO')