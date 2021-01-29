x1,y1 = map(int,input().split(" "))
x2,y2 = map(int,input().split(" "))
t = int(input())
check = abs(x2-x1)+abs(y2-y1)-t
if check % 2 == 1 or check > 0:
    print("N")
else:
    print("Y")