from functools import*;w=[input().lower()for _ in'.'*int(input())]
@cache
def f(s,i):return sum(f(s,i+len(x))for x in w if s[i:i+len(x)]==x)if i-len(s)else 1
for _ in'.'*int(input()):print(f(input(),0))