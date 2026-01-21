from bisect import*;I=input;n,q=map(int,I().split());Q=sorted(map(int,I().split()))
for _ in'.'*n:c,*v=I().split();insort(Q,int(*v))if'D'>c else print(Q.pop(-('Q'<c)))