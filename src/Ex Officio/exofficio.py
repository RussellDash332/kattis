R, C = map(int, input().split()); print(' _'*C)
if R == 1: print('|'+'_ '*(C-1)+'_|'), exit(0)
if C == 1: print('| |\n'*(R-1)+'|_|'), exit(0)
# edge case if R is odd and C is even, need to add bar in middle
for i in range(R-1): print('|'+'_ '*(C//2-1)+['_ ', [' |', '  '][i==(R-1)//2]][R%2 and C%2==0]+' '+' _'*(C-C//2-1)+'|')
print('|'+'_ '*(C//2-1)+'_'+' |'[R%2 and C%2==0]+'_ '*(C-C//2-1)+'_|')