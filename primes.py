def primes(n):
    if n < 2: return -1

    array = [False, False] + [True] * (n-2)
    primes = []

    for i in range(n):
        if array[i] == True:
            primes.append(i)
            for j in range(i+1, n):
                if j % i == 0: array[j] = False

    return primes

n = int(input('Enter a number: '))
print(primes(n))
