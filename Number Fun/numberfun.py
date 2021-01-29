q = int(input())
for _ in range(q):
    a,b,c = list(map(int,input().split(" ")))
    if a+b==c or abs(a-b)==c or a*b==c or a*c==b or b*c==a:
        print("Possible")
    else:
        print("Impossible")