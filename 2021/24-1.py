from itertools import product

f = open('2021/inputs/24.txt')
lines = f.read().splitlines()


def construct_ups_downs():
    global lines
    ups = [None for _ in range(14)]
    downs = [None for _ in range(14)]
    num = 0
    index = 0
    for idx, line in enumerate(lines):
        if idx == 0 or line == 'inp w':
            index = 0

        if index == 5 and line.startswith('add'):
            op = line.split()
            if int(op[2]) > 0:
                ups[num] = int(lines[idx + 10].split()[2])
            else:
                downs[num] = int(op[2])

            num += 1
        index += 1
    return ups, downs


def works(number, ups, downs):
    z = 0
    res = [0 for _ in range(14)]
    idx = 0

    for i in range(14):
        up, down = ups[i], downs[i]

        if up is not None:
            z = 26 * z + number[idx] + up
            res[i] = str(number[idx])
            idx += 1

        if down is not None:
            res[i] = ((z % 26) + down)
            z //= 26
            if not (1 <= res[i] <= 9):
                return None
            res[i] = str(res[i])

    return res


numbers = product(range(9, 0, -1), repeat=7)
ups, downs = construct_ups_downs()
for number in numbers:
    res = works(number, ups, downs)
    if res is not None:
        print(res)
        print(''.join(res))
        break
