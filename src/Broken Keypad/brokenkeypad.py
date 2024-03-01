# the number of integers in [0, n] that contain the digit 7
def f(n):
    ans = 0
    for i in range(len(n)):
        p = len(n)-i-1; c = int(n[i]); s = f('9'*p)                 # 0 to 9...9
        if c > 7:       ans += (c-1)*s + 10**p                      # ([0, 69...9] + [80...0, (c-1)9...9]) + [70...0, 79...9]
        elif c < 7:     ans += c*s                                  # [0, (c-1)9...9] = [0, 9...9] * c
        else:           return ans + 7*s + (1 + int(n[i+1:] or 0))  # [0, 69...9] + [70...0, 7{n[i+1:]}]
    return ans

a, b = map(int, input().split())
print(f(str(b))-f(str(a-1)))