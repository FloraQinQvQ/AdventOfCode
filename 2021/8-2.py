data = []
with open('./2021/inputs/8.txt') as f:
    line = f.readline()
    while line:
        left = sorted([''.join(sorted(x)) for x in line.strip('\n').split('|')[0].split()], key=len)
        right = [''.join(sorted(x)) for x in line.strip('\n').split('|')[1].split()]

        data.append([left, right])
        line = f.readline()


def sub_string(a, b):
    count = ''
    for char in a:
        if char in b:
            count += char
    return count


entiretotal = 0
for problem in data:
    left = problem[0]
    # 1 4 7 8
    setup = {left[0]: 1, left[1]: 7, left[2]: 4, left[9]: 8}
    # 3, 2, 5
    fives = [left[3], left[4], left[5]]
    # 6, 0, 9
    sixes = [left[6], left[7], left[8]]

    # 6
    for idx in range(len(sixes)):
        if len(sub_string(left[0], sixes[idx])) == 1:
            setup[sixes[idx]] = 6
            del(sixes[idx])
            break

    # 3
    for idx in range(len(fives)):
        if len(sub_string(left[0], fives[idx])) == 2:
            setup[fives[idx]] = 3
            del(fives[idx])
            break

    # 9
    for idx in range(len(sixes)):
        if len(sub_string(left[2], sixes[idx])) == 4:
            setup[sixes[idx]] = 9
            del(sixes[idx])
            break

    # 0
    setup[sixes[0]] = 0

    # 2
    for idx in range(len(fives)):
        if len(sub_string(left[2], fives[idx])) == 2:
            setup[fives[idx]] = 2
            del(fives[idx])
            break

    # 5
    setup[fives[0]] = 5

    total = 0
    for digit in problem[1]:
        print(problem[1])
        print(digit)
        total *= 10
        total += setup[digit]
    entiretotal += total

print(entiretotal)

