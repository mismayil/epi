def can_reach(array):
    if len(array) == 1: return True

    if array[0] == 0: return False

    furthest = 0
    i = 0

    while True:
        if i <= furthest and furthest < len(array)-1:
            furthest = max(furthest, i + array[i])
        else:
            break

        i += 1

    return True if furthest >= len(array)-1 else False

elems = input('Enter array: ')
array = list(map(lambda x: int(x), elems.split(' ')))
print(can_reach(array))
