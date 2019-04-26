def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def reorder(array, index):
    pivot = array[index]
    sindex = 0
    lindex = len(array)-1

    for i in range(len(array)):
        if array[i] < pivot:
            swap(array, sindex, i)
            sindex += 1

    for i in range(len(array)):
        if array[i] > pivot:
            swap(array, lindex, i)
            lindex -= 1

    return array

elems = input('Enter array:')
index = int(input('Enter pivot index:'))
array = list(map(lambda x: int(x), elems.split(' ')))
print(reorder(array, index))
