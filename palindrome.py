import math

def is_palindromic(number):
    if number < 0: return False
    
    size = int(math.log10(number)) + 1
    msdmask = 10 ** (size-1)
    lsdmask = 10

    for i in range(0, size // 2):
        if (number // msdmask) != (number % lsdmask): return False
        number %= msdmask
        number //= lsdmask
        msdmask //= 100


    return True

number = int(input('Enter number:'))
print(is_palindromic(number))
