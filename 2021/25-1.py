from copy import deepcopy

f = open('2021/inputs/25.txt')
lines = f.read().splitlines()
matrix = [list(line) for line in lines]

row = len(matrix)
col = len(matrix[0])


def move(matrix, type):
    next_matrix = deepcopy(matrix)
    anymoves = False

    for i in range(row):
        for j in range(col):
            if type != matrix[i][j]:
                continue

            if matrix[i][j] == 'v':
                next_i, next_j = (i + 1) % row, j
            else:
                next_i, next_j = i, (j + 1) % col

            if matrix[next_i][next_j] == '.':
                next_matrix[next_i][next_j] = matrix[i][j]
                next_matrix[i][j] = '.'
                anymoves = True
    return next_matrix, anymoves


step = 0
while True:
    matrix, anymoves_e = move(matrix, '>')
    matrix, anymoves_s = move(matrix, 'v')
    step += 1
    if not anymoves_e and not anymoves_s:
        print(step)
        break
