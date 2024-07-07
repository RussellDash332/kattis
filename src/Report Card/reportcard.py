R = {
    'A': [0, 0, -3],
    'B': [3, 0, -3],
    'C': [3, 0, -3],
    'D': [3, 0, -3],
    'F': [0]
}
M = 10**9+7; N = int(input()); Z = [0]*18001; Z[9000] = 1
for i in input():
    X = [0]*18001
    for j in R[i]:
        for k in range(18001):
            if 0<=k+j<18001: X[k+j] = (X[k+j]+Z[k])%M
    Z = X
print(sum(Z[9001:])%M)