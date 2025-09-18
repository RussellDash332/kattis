from bisect import*;n,q=map(int,input().split());t=[]
for _ in'.'*q:
 c,*v=input().split()
 if'-'>c:t.remove(int(v[0]))
 elif'?'>c:insort(t,int(v[0]))
 else:l,r=map(int,v);a=bisect_left(t,l);b=bisect_left(t,r);print('im'*any([a<len(t)and t[a]==l,b<len(t)and t[b]==r,t and(a-b)%len(t)])+'possible')