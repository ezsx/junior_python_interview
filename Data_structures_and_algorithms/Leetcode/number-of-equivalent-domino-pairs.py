def check(i, j):
    return (i[0] == j[0] and i[1] == j[1]) or \
           (i[0] == j[1] and i[1] == j[0])


dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]

count = 0
for i in range(len(dominoes)):
    for j in range(i+1, len(dominoes)):
        if check(dominoes[i], dominoes[j]):
            count += 1
print(count)
