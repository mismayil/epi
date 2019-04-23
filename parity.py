def parity1(number):
    ones = 0

    while number != 0:
        mask = number & 1
        if mask == 1: ones += 1
        number = number >> 1

    if ones % 2 == 0: return 1
    return 0

def parity2(number):
    ones = 0

    while number != 0:
        mask = number & ~(number-1)
        number = number ^ mask
        ones += 1

    if ones % 2 == 0: return 1
    return 0

def parity3(number):
    number ^= number >> 32
    number ^= number >> 16
    number ^= number >> 8
    number ^= number >> 4
    number ^= number >> 2
    number ^= number >> 1
    return number & 1

number = int(input('Enter number:'), 2)
print(parity3(number))
