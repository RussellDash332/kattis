L = []
for _ in range(int(input())):
    s = input().lower()
    if s in L or '1'*7 in ''.join('01'[x in 'bcdfghjklmnpqrstvwxyz'] for x in s): print('no'); continue
    L = L[-9:]+[s]; print('yes')