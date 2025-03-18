def f(x, y):
    x, y = abs(x), abs(y)
    if x+y==1: return 3
    if x*y==1: return 2
    if x==y==2: return 4
    if x>y: x,y=y,x
    if y>=2*x: return (y+1)//2+(y//2-x)%2
    return sum(divmod(x+y,3))
while True:
    try: print(f(*map(int, input().split())))
    except: break