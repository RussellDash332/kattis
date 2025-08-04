K,S=map(eval,input().split())
for _ in'.'*int(input()):d,x,y,z=map(float,input().split());print((abs(S-x)+abs(y)+abs(z))*K/S*d)