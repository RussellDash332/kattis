for _ in range(int(input())):
    isbn = input().strip()
    cuts = [*map(len, isbn.split('-'))]
    if sum(cuts) != 10 or (len(cuts) == 4 and cuts[3] != 1) or (len(cuts) > 4) or (0 in cuts) or ('X' in isbn[:-1]): print('invalid'); continue
    cs = 0
    for i, d in enumerate(isbn.replace('-', '')): cs += (10-i)*int(d if d != 'X' else 10)
    if cs % 11: print('invalid'); continue
    cs = 8
    for i, d in enumerate(isbn.replace('-', '')[:-1]): cs += (3-2*(i%2))*int(d)
    print(f'{978}-{isbn[:-1]}{-cs%10}')