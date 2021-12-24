f = open('2021/inputs/20.txt')
lines = f.read().splitlines()

enhancement_algo = lines[0]
lines = lines[2:]

init_row = len(lines)
init_col = len(lines[0])
matrix = {}
for i in range(init_row):
    for j in range(init_col):
        matrix[(i, j)] = lines[i][j]


def enhancing(matrix, init_row, init_col, times=2):
    for _ in range(times):
        nd = {}
        for i in range(-2 * times, init_row + 2 * times):
            for j in range(-2 * times, init_col + 2 * times):
                pixels = ''
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        ii = i + dx
                        jj = j + dy

                        if (ii, jj) in matrix and matrix[(ii, jj)] == '#':
                            pixels += '1'
                        else:
                            pixels += '0'
                nd[(i, j)] = enhancement_algo[int(pixels, 2)]
        matrix = nd
    return len([key for key in matrix if matrix[key] == '#' and -times <= key[0] <= init_row + times - 1 and -times <= key[1] <= init_col + times - 1])


print(enhancing(matrix, init_row, init_col, 2))
