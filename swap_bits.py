def swap(number, i, j):
    inum = (number >> i) & 1
    jnum = (number >> j) & 1

    if inum == jnum: return number

    imask = 1 << i
    jmask = 1 << j
    return number ^ (imask | jmask)

number = int(input('Enter number:'), 2)
ij = input('Enter i, j:')
i, j = map(lambda x: int(x), ij.split(' '))
print(format(swap(number, i, j), 'b'))
