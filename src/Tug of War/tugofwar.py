n = int(input()); s = sum(p:=[int(input()) for _ in range(n)]); dp = [1]+n//2*[0]
for w in p:
    for i in range(n//2-1, -1, -1): dp[i+1] |= dp[i]<<w
z = dp[n//2]; k = s//2; a = z&((1<<(k+1))-1); b = z>>(k+1); lo = a.bit_length()-1; hi = k+1+(b&-b).bit_length()-1 if b else lo; left = lo if s-2*lo <= 2*hi-s else hi; print(min(s-left, left), max(s-left, left))