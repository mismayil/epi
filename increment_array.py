def increment(array):
    carry = 1

    for i in range(len(array)-1, -1, -1):
        sum = array[i] + carry

        if sum < 10:
            array[i] = sum
            carry = 0
        else:
            array[i] = 0
            carry = 1

    if carry == 1: return [1] + array
    return array

elems = input('Enter array: ')
array = list(map(lambda x: int(x), elems.split(' ')))
print(increment(array))
