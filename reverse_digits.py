def reverse(number):
    remainder = abs(number)
    result = 0

    while remainder != 0:
        result = result * 10 + remainder % 10
        remainder //= 10

    return -result if number < 0 else result

number = int(input('Enter number:'))
print(reverse(number))
