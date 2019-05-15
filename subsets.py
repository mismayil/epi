def subsets_all(set):
    print([])

    for i in range(len(set)):
        subsets(set[i+1:], [set[i]])

def subsets(rest, subset):
    print(subset)

    for i in range(len(rest)):
        subsets(rest[i+1:], subset + [rest[i]])

set = [int(i) for i in input('Enter an array: ').split(',')]
subsets_all(set)
