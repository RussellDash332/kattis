X='NCCCCQQQQGGGGGFGGGGGQQQCCCCC';N=int(input());W=[input()[0]for _ in'.'*N]
for i in range(1,29):
 if all(X[i*-~k%28]==W[k]for k in range(N)):print(i);exit()