def equal(a, b): # floating point issue
    return abs(a-b) < 1e-5

def leading_entry_col(A, r): # given A[r], what's the first nonzero index/column
    row = A[r]
    i = 0
    while i < len(A[0]) and equal(row[i], 0): i += 1
    return i

def list_pivots(A):
    res = []
    for r in range(len(A)):
        k = leading_entry_col(A, r)
        if k != len(A[0]): res.append((r, k))
    res.sort(reverse=True)
    return res

def col(A, i):
    return list(map(lambda x: x[i], A))

def ero1(A, i, c): # cRi, modifies A
    for j in range(len(A[0])): A[i][j] *= c

def ero2(A, i, j, c): # Ri + cRj, modifies A
    for k in range(len(A[0])): A[i][k] += c*A[j][k]

def ero3(A, i, j): # swap Ri and Rj, modifies A
    A[i], A[j] = A[j], A[i]

def rref(A): # modifies A and returns the RREF of A
    # start from A_{1,1}
    curr_col = 0
    curr_row = 0
    while curr_col < len(A[0]) and curr_row < len(A): # while the pointer points to an entry in the matrix
        if equal(A[curr_row][curr_col], 0): # current entry is 0, we want to make it 1 by swapping with a non-zero entry
            check_col = col(A, curr_col)[curr_row+1:] # check all the entries below it
            for i in range(len(check_col)):
                if not equal(check_col[i], 0): break
                elif i == len(check_col)-1: i += 1
            if i < len(check_col): # if found a non-zero entry in that column, swap with that row
                ero3(A, curr_row, curr_row+i+1)
            else: # otherwise, all the entries in that column is zero, move on to the next column
                '''
                The case would be something like this
                0  1 2
                0 -1 3
                0  2 4
                '''
                curr_col += 1
        else: # the entry is nonzero, do ero1 and/or ero2
            # make the current entry 1 first by doing ero1
            # now, A[curr_row][curr_col] = 1
            if not equal(A[curr_row][curr_col], 1): ero1(A, curr_row, 1/A[curr_row][curr_col])
            '''
            Now we know the augmented matrix is something like this
            1  0 3 -> the leading entry must be 1
            4 -1 9
            3  7 5
            '''
            # for all rows below it, do ero2
            for i in range(curr_row+1, len(A)):
                if not equal(A[i][curr_col], 0): ero2(A, i, curr_row, -A[i][curr_col])
            '''
            Using the previous example, we want the augmented matrix to be something like this
            1  0 3 -> the leading entry must be 1
            0 -1 -3
            0  7 -4
            '''
            curr_col += 1
            curr_row += 1

    # Now that it's all REF, let's bring it to RREF!
    pivots = list_pivots(A) # work from bottom to top
    for i in range(len(pivots)-1):
        for j in range(pivots[i][0]-1, -1, -1): # j < pr[i][0]
            ero2(A, j, pivots[i][0], -A[j][pivots[i][1]])
    return A

n = -1
while n != 0:
    n = int(input())
    if n != 0:
        A = [list(map(float, input().split())) for _ in range(n)]
        r = list(map(float, input().split()))
        for i in range(n): A[i].append(r[i]) # make augmented matrix
        A = rref(A)
        pv = list_pivots(A)
        if pv:
            if pv[0][1] == n: print('inconsistent')
            elif len(pv) == n:
                for i in range(n): print(A[i][n], end=' ')
                print()
            else:
                ans = ['?']*n
                for r, c in pv:
                    oz = True
                    for k in range(c+1, n):
                        if not equal(A[r][k], 0): oz = False; break
                    if oz: ans[c] = str(A[r][n])
                print(' '.join(ans))
        else:
            # no pivot column, a zero matrix!
            print('? '*n)