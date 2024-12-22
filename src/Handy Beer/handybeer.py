l = 'yuiophjklnm,.'; t, s = map(int, input().split())
S = input(); a = b = 0
for i in S:
    if i == ' ':    a, b, = a+t, b+t
    elif i in l:    a, b = a+t, b+1000
    else:           a, b = a+1000, b+t
    a, b = min(a, b+s), min(b, a+s)
print(min(a, b))