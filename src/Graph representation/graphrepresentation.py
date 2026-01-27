I=input
for _ in'.'*int(I()):print(int(I())+1-(sum(a*b for a,b in zip(map(int,I().split()),map(int,I().split())))or 1))