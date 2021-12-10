f = open('./2021/inputs/1.txt')
content = f.read()
depths = content.splitlines()
depths = [int(i) for i in depths]

total_increases = 0
sum = depths[0] + depths[1] + depths[2]
for idx, depth in enumerate(depths):
    if idx <= 2:
        continue

    if sum + depth - depths[idx - 3] > sum:
        total_increases += 1

    sum = sum + depth - depths[idx - 3]

print(total_increases)
