from pprint import pprint
f = open('./2021/inputs/5.txt')
content = f.read()
contents = content.splitlines()

coordinates = []
max_x = 0
max_y = 0
for content in contents:
    start = content.split('->')[0].strip()
    end = content.split('->')[1].strip()
    x1 = int(start.split(',')[0].strip())
    y1 = int(start.split(',')[1].strip())
    x2 = int(end.split(',')[0].strip())
    y2 = int(end.split(',')[1].strip())
    max_x = max([x1, x2, max_x])
    max_y = max([y1, y2, max_y])
    coordinates.append((x1, y1, x2, y2))

matrix = [[0 for _ in range(max_y+1)] for _ in range(max_x+1)]


def diagonal(x1, y1, x2, y2):
    a = (y1-y2)/(x1-x2)
    b = y1-a*x1

    return a, b


for coordinate in coordinates:
    x1, y1, x2, y2 = coordinate
    if x1 != x2 and y1 != y2:
        if abs(x1-x2)/abs(y1-y2) != 1:
            continue
        else:
            a, b = diagonal(x1, y1, x2, y2)
            if x1 < x2:
                x = x1 + 1
                y = int(a*x + b)
                while y != y2:
                    matrix[x][y] += 1
                    x = x + 1
                    y = int(a*x + b)
            else:
                x = x1 - 1
                y = int(a*x + b)
                while y != y2:
                    matrix[x][y] += 1
                    x = x - 1
                    y = int(a*x + b)
    matrix[x1][y1] += 1
    matrix[x2][y2] += 1

    if x1 == x2 and y1 > y2:
        y = y2 + 1
        while y < y1:
            matrix[x1][y] += 1
            y += 1
    elif x1 == x2 and y1 < y2:
        y = y1 + 1
        while y < y2:
            matrix[x1][y] += 1
            y += 1
    elif y1 == y2 and x1 > x2:
        x = x2 + 1
        while x < x1:
            matrix[x][y1] += 1
            x += 1
    elif y1 == y2 and x1 < x2:
        x = x1 + 1
        while x < x2:
            matrix[x][y1] += 1
            x += 1
total = 0
for i in range(max_x+1):
    for j in range(max_y+1):
        if matrix[i][j] >= 2:
            total += 1


pprint(total)
