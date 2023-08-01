def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    i = find(i)
    j = find(j)
    if size[i] < size[j]:
        (i, j) = (j, i)
    size[i] += size[j]
    parent[j] = i

(n, m) = list(map(int, input().split()))
size = [1] * n
parent = list(range(n))
answer = n
for _ in range(m):
    (u, v) = list(map(int, input().split()))
    u -= 1
    v -= 1
    if find(u) != find(v):
        answer -= 1
    union(u, v)
print(answer)