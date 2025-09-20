n,l=map(int,input().split());d=[L:=0,*map(int,input().split()),l];w=[0,*map(int,input().split()),0];H=1e9
while H-L>1e-7:
 v=(L+H)/2;t=[0]
 for i in range(1,n+2):t+=[max(d[i],t[i-1]+w[i-1]+(d[i]-d[i-1])/v)]
 if t[-1]>l:L=v
 else:H=v
print(['IMPOSSIBLE',v][v<1e9])