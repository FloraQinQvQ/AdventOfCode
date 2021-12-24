f = open('2021/inputs/22.txt')
lines = f.read().splitlines()

target_ranges = []

for line in lines:
    isturnon = line.startswith('on')
    x = line.split('on x=')[1].split(
        ',y=') if isturnon else line.split('off x=')[1].split(',y=')
    y_z = x[1].split(',z=')

    # on x=10..12,y=10..12,z=10..12
    x_range = (int(x[0].split('..')[0]), int(x[0].split('..')[1]))
    y_range = (int(y_z[0].split('..')[0]), int(y_z[0].split('..')[1]))
    z_range = (int(y_z[1].split('..')[0]), int(y_z[1].split('..')[1]))

    target_range = (x_range, y_range, z_range, isturnon)
    target_ranges.append(target_range)


max_range = (-50, 50)
final = set()
for target_range in target_ranges:
    x0 = max(target_range[0][0], max_range[0])
    x1 = min(target_range[0][1], max_range[1])
    y0 = max(target_range[1][0], max_range[0])
    y1 = min(target_range[1][1], max_range[1])
    z0 = max(target_range[2][0], max_range[0])
    z1 = min(target_range[2][1], max_range[1])

    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            for t in range(z0, z1 + 1):
                if target_range[3]:
                    final.add((i, j, t))
                else:
                    if (i, j, t) in final:
                        final.remove((i, j, t))

print(len(final))
