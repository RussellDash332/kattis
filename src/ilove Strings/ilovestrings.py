M = {e:i for i,e in enumerate('aeiouAEIOUbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')}
S = [M[i] for i in input()]; N = len(S); P = 10**9+7
Q = [0]*10; R = [0]*10; F = [0]*420; B = [0]*420; Z = A = 0; V = [0]*10; C = [0]*42
for i in range(N):
    if S[i] < 10: Q[S[i]] += 1
    else:
        for j in range(10): F[42*j+S[i]-10] += Q[j]
for i in range(N-1, -1, -1):
    if S[i] < 10:
        Q[S[i]] -= 1 # num of v1 before i
        R[S[i]] += 1 # num of v1 not before i
        '''
        Given v3, for every (v1!=v3, c2) from the front, we need to find the number of (c4, v5) pairs at the back
        Inclusion exclusion to count invalid pairs:
        |v5==v1| + |v5==v3| + |c2==c4| - |v5==v1, c2==c4| - |v5==v3, c2==c4|
        '''
        for j in range(10): # v1
            if j == S[i]: continue
            for k in range(42): # c2
                Z += F[42*j+k]*(A-V[j]-V[S[i]]-C[k]+B[42*j+k]+B[42*S[i]+k]); Z %= P
    else:
        for j in range(10):
            F[42*j+S[i]-10] -= Q[j] # number of (v1 then c2) before i
            B[42*j+S[i]-10] += R[j] # number of (v1 then c2) not before i
            A += R[j]               # number of (v, c) pairs not before i
            C[S[i]-10] += R[j]      # number of (v, c2) pairs not before i
            V[j] += R[j]            # number of (v1, c) pairs not before i
print(Z%P)