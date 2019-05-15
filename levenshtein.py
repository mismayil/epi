def levenshtein(a, b):
    m = len(a)
    n = len(b)

    if m == 0: return n
    if n == 0: return m

    distances = [[j if i == 0 else 0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        distances[i][0] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            distances[i][j] = min(distances[i-1][j] + 1, distances[i][j-1] + 1, distances[i-1][j-1] + (0 if a[i-1] == b[j-1] else 1))

    print(distances)
    return distances[m][n]

a, b = input('Enter strings: ').split(',')
print(levenshtein(a.strip(), b.strip()))
