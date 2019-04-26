import random

def random_subset(n, k):
    mapping = {}

    for i in range(k):
        randindex = random.randint(i, n-1)
        m1 = mapping.get(randindex)
        m2 = mapping.get(i)

        if m1 == None and m2 == None:
            mapping[randindex] = i
            mapping[i] = randindex
        elif m1 == None and m2 != None:
            mapping[randindex] = m2
            mapping[i] = randindex
        elif m1 != None and m2 == None:
            mapping[i] = m1
            mapping[randindex] = i
        else:
            mapping[i] = m1
            mapping[randindex] = m2

    return list(mapping.values())[:k]

n = int(input('Enter n: '))
k = int(input('Enter k: '))
print(random_subset(n, k))
