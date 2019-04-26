import random

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def sample(array, k):
    for i in range(k):
        randindex = random.randint(i, len(array))
        swap(array, i, randindex)

    return array[:k]

elems = input('Enter array: ')
k = int(input('Enter k:'))
array = list(map(lambda x: int(x), elems.split(' ')))
print(sample(array, k))
