q = int(input())
for _ in range(q):
    a = input()
    b = input()
    res = ""
    for i in range(len(a)):
        if a[i]==b[i]:
            res += "."
        else:
            res += "*"
    print(a)
    print(b)
    print(res)
    print()