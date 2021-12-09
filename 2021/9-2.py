from pprint import pprint

row = col = 0
file = './2021/9.txt'
# file = './2021/9-sample.txt'
with open(file) as f:
    line = f.readline()
    col = len(line.strip())
    row += 1
    while line:
        line = f.readline()
        if line.strip()!='':
            row += 1

matrix = [[0 for _ in range(col)] for _ in range(row)]
footprint = [[0 for _ in range(col)] for _ in range(row)]

with open(file) as f:
    line = f.readline()
    for idx, ele in enumerate(line.strip()):
        matrix[0][idx] = int(ele)
    row = 1
    while line:
        line = f.readline()
        if line.strip()!='':
            for idx, ele in enumerate(line.strip()):
                matrix[row][idx] = int(ele)
            row += 1

data = []
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        flag = False
        for direction in directions:
            ii = i + direction[0]
            jj = j + direction[1]
            if ii < 0 or jj < 0 or ii > len(matrix)-1 or jj > len(matrix[0])-1:
                continue
            if matrix[i][j] >= matrix[ii][jj]:
                flag = True
        if flag == False:
            data.append((i, j))


def get_size(matrix, i,j, direction, size = 0):
    ii = i + direction[0]
    jj = j + direction[1]
    if ii < 0 or jj < 0 or ii > len(matrix)-1 or jj > len(matrix[0])-1:
        return size
    if matrix[ii][jj] == 9:
        return size
    
    if matrix[i][j] < matrix[ii][jj] and footprint[ii][jj] != 1:
        size += 1
        footprint[ii][jj] = 1
        for direct in directions:
            if direct[0]==-direction[0] and direct[1]==-direction[1]:
                continue
            size = get_size(matrix, ii, jj, direct, size)
    return size
total = []
for datum in data:
    size = 1
    for direction in directions:
        size = get_size(matrix, datum[0], datum[1], direction, size)
    total.append(size)

total = sorted(total, reverse=True)
# 1391940
print(total[0] * total[1]* total[2])