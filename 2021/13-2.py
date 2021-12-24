from pprint import pprint
f = open('2021/inputs/13.txt')
lines = f.read().splitlines()

folds = []
row = col = 0
for line in lines:
    if line.startswith('fold along'):
        folds.append(line.split('fold along ')[1])
    elif line.strip() == '':
        continue
    else:
        coords = line.split(',')
        row = max([int(coords[0]), row])
        col = max([int(coords[1]), col])
row += 1
col += 1

matrix = [['.' for _ in range(col)] for _ in range(row)]

for line in lines:
    if line.startswith('fold along') or line.strip() == '':
        continue
    else:
        coords = line.split(',')
        matrix[int(coords[0])][int(coords[1])] = '#'

remaining_row = row
remaining_col = col

for fold in folds:
    if fold.startswith('y'):
        num = int(fold.split('y=')[1])

        for x in range(row):
            for y in range(num + 1, col):
                if matrix[x][y] == '#':
                    matrix[x][num - (y-num)] = '#'
                    matrix[x][y] = '.'
        remaining_col = num - 1
    else:
        num = int(fold.split('x=')[1])

        for y in range(col):
            for x in range(num+1, row):
                if matrix[x][y] == '#':
                    matrix[num - (x-num)][y] = '#'
                    matrix[x][y] = '.'
        remaining_row = num - 1

remaining_row += 1
remaining_col += 1
remaining_matrix = [['.' for _ in range(remaining_col)]
                    for _ in range(remaining_row)]
for i in range(remaining_row):
    for j in range(remaining_col):
        remaining_matrix[i][j] = matrix[i][j]
pprint(remaining_matrix)
