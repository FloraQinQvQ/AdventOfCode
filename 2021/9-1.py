row = col = 0
file = './2021/inputs/9.txt'
with open(file) as f:
    line = f.readline()
    col = len(line.strip())
    row += 1
    while line:
        line = f.readline()
        if line.strip()!='':
            row += 1

matrix = [[0 for _ in range(col)] for _ in range(row)]

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
            data.append(matrix[i][j])

print(sum([ele + 1 for ele in data]))



