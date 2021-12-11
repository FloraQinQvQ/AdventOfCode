from pprint import pprint

f = open('./2021/inputs/11-sample.txt')
# f = open('./2021/inputs/11.txt')
lines = f.read().splitlines()

row = len(lines)
col = len(lines[0].strip())

matrix = [[0 for _ in range(col)] for _ in range(row)]

for i, line in enumerate(lines):
    for j, ele in enumerate(line.strip()):
        matrix[i][j] = int(ele)

directions = [[-1, 0], [1, 0], [0, -1], [0, 1],
              [1, 1], [-1, -1], [1, -1], [-1, 1]]

flashes = 0


def count_flashes(matrix, i, j):
    global flashes
    flashes += 1
    matrix[i][j] = -1

    for direction in directions:
        ii = i + direction[0]
        jj = j + direction[1]
        if ii < 0 or jj < 0 or ii > len(matrix) - 1 or jj > len(matrix[0]) - 1 or matrix[ii][jj] == -1:
            continue
        else:
            matrix[ii][jj] += 1
            if matrix[ii][jj] > 9:
                matrix[ii][jj] = -1

                count_flashes(matrix, ii, jj)
    return flashes


for step in range(100):
    for i in range(row):
        for j in range(col):
            matrix[i][j] += 1

    for i in range(row):
        for j in range(col):
            if matrix[i][j] > 9 and matrix[i][j] != -1:
                count_flashes(matrix, i, j)

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

# 1656
pprint(matrix)
pprint(flashes)
