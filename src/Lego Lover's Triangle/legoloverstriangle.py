a, b = map(int, input().split())
def f(a, b):
    x = y = 0
    for i in range(a):
        x += max((b*i//a-2*(i%2))//4, 0)
        y += max((b*i//a-2*(1-i%2))//4, 0)
    return max(x, y)
print(max(f(a, 2*b), f(b, 2*a)))