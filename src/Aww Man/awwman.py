I=input
for _ in'.'*int(I()):n,m=map(int,I().split());a,b,d=map(int,I().split());print('YNEOS'[(2*b+d-a)%n>n-m::2])