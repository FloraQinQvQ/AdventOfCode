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


Xs = []
Ys = []
Zs = []

for target_range in target_ranges:
    Xs.extend([target_range[0][0], target_range[0][1] + 1])
    Ys.extend([target_range[1][0], target_range[1][1] + 1])
    Zs.extend([target_range[2][0], target_range[2][1] + 1])

Xs = sorted(list(set(Xs)))
Ys = sorted(list(set(Ys)))
Zs = sorted(list(set(Zs)))

grid = [[[0 for _ in range(len(Zs))] for _ in range(len(Ys))]
        for _ in range(len(Xs))]

for target_range in target_ranges:
    x0 = Xs.index(target_range[0][0])
    x1 = Xs.index(target_range[0][1] + 1)
    y0 = Ys.index(target_range[1][0])
    y1 = Ys.index(target_range[1][1] + 1)
    z0 = Zs.index(target_range[2][0])
    z1 = Zs.index(target_range[2][1] + 1)

    for i in range(x0, x1):
        for j in range(y0, y1):
            for t in range(z0, z1):
                grid[i][j][t] = 1 if target_range[3] else 0

ans = 0
for i in range(len(Xs) - 1):
    for j in range(len(Ys) - 1):
        for t in range(len(Zs) - 1):
            ans += grid[i][j][t] * (Xs[i + 1] - Xs[i]) * \
                (Ys[j + 1] - Ys[j]) * (Zs[t + 1] - Zs[t])

print(ans)
