import string

def convertbase(numstr, source, target):
    number = 0
    negative = numstr.startswith('-')
    n = len(numstr)

    for i in range(1 if negative else 0, n):
        number += int(numstr[i]) * (source ** (n-i-1))

    if number == 0: return '0'

    if target == 1: return '-1' + '1' * number if negative else '1' * number

    converted = ''

    while number != 0:
        rem = number % target

        if rem > 9: converted = string.ascii_uppercase[rem%10] + converted
        else: converted = str(rem) + converted

        number //= target

    return '-' + converted if negative else converted

numstr = input('Enter number: ')
source = int(input('Enter source base: '))
target = int(input('Enter target base: '))
print(convertbase(numstr, source, target))
