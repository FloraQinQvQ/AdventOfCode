import itertools
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
folds = [folds[0]]
for fold in folds:
    if fold.startswith('y'):
        num = int(fold.split('y=')[1])

        for x in range(row):
            for y in range(num+1, col):
                if matrix[x][y] == '#':
                    matrix[x][num - (y-num)] = '#'
                    matrix[x][y] = '.'

    else:
        num = int(fold.split('x=')[1])

        for y in range(col):
            for x in range(num+1, row):
                if matrix[x][y] == '#':
                    matrix[num - (x-num)][y] = '#'
                    matrix[x][y] = '.'


print([x for x in itertools.chain(*matrix) if x == '#'])
print(len([x for x in itertools.chain(*matrix) if x == '#']))
