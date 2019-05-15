def permute_all(array):
    for i in range(len(array)):
        rest = array[:]
        rest.pop(i)
        permute(array[i], rest, [])

def permute(elem, rest, permutation):
    if rest == []:
        print(permutation)
        return

    for i in range(len(rest)):
        r = rest[:]
        r.pop(i)
        p = permutation[:]
        p.append(elem)
        permute(rest[i], r, p)

array = [int(n) for n in input('Enter array: ').split(',')]
permute_all(array)
