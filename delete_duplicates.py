def delete_dups(array):
    aval_index = 1

    for i in range(1, len(array)):
        if array[i] != array[i-1]:
            array[aval_index] = array[i]
            aval_index += 1

    return array

elems = input('Enter array:')
array = list(map(lambda x: int(x), elems.split(' ')))
print(delete_dups(array))
