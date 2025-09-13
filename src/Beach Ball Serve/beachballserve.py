def X(a):
 x=0;y=H;v=V*cos(a);w=V*sin(a);t=1e-5
 while y>0:v-=v*R*t;w-=(w*R+G)*t;x+=v*t;y+=w*t
 return x
def W(z):
 y=sqrt(2*exp(1)*z+2)-1if exp(-1)+z<=1else log((z+1)/log(z+1))
 while abs(m:=(y*exp(y)-z)/(exp(y)+y*exp(y)))>1e-8:y-=m
 return y
from math import*;V,H,R=map(int,input().split());G=981;R*=.01;T=-(W((V*V*R*R/G/G-1)*exp(-H*R*R/G-1))*G+H*R*R+G)/G;print(X(a:=-asin((H+G/R/R*(T+(1-exp(T))))/(V/R*(1-exp(T))))),a*180/pi)