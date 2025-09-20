n,l=map(int,input().split());d=[0,*map(int,input().split()),l];w=[0,*map(int,input().split()),0];v=int(input());t=[0]
for i in range(1,n+2):t+=[max(d[i],t[i-1]+w[i-1]+(d[i]-d[i-1])/v)]
print('YNEOS'[t[-1]>l::2])