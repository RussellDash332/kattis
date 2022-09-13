n = int(input())
if n % 100 == 49:
    print(n + 50)
else:
    print(max(99, min([n//100*100 - 1, n//100*100 + 99], key=lambda x: abs(x-n))))