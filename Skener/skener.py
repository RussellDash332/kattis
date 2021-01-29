r, c, zr, zc = map(int,input().split(" "))
for _ in range(r):
    row = input()
    zrow = ""
    for i in range(c):
        zrow += row[i]*zc
    for _ in range(zr):
        print(zrow)