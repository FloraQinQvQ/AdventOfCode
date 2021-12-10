f = open('./2021/inputs/3.txt')
content = f.read()
inputs = content.splitlines()


def get_map(inputs):
    map = [0] * len(inputs[0])
    for idx, input in enumerate(inputs):
        for index, i in enumerate(input):
            if i == '0':
                map[index] -= 1
            else:
                map[index] += 1
    return map

map = get_map(inputs)
aa = inputs.copy()
idx = 0
while len(aa) != 1:
    aa = [a for a in aa if (map[idx] >= 0 and a[idx] == '1') or (map[idx] < 0 and a[idx] == '0')]
    map = get_map(aa)
    idx += 1

map = get_map(inputs)
bb = inputs.copy()
idx = 0
while len(bb) != 1:
    bb = [b for b in bb if (map[idx] >= 0 and b[idx] == '0') or (map[idx] < 0 and b[idx] == '1')]
    map = get_map(bb)
    idx += 1

oxygen = int(aa[0], 2)
co2 = int(bb[0], 2)

print(oxygen, co2)
print(oxygen*co2)
